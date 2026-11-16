"""Render the public website to plain HTML so it can be hosted on GitHub Pages.

GitHub Pages only serves static files, so this command runs the real Django
views through the test client, rewrites every URL to a relative one (the site
lives under /<repo>/ on project pages), and copies the static assets alongside.

What is exported:

* every public page, for both themes and both languages
* one folder per project / suburb / service / news post
* replacement copies of asset files with theme + language overlays baked in

The theme/language overlays exist because there is no server to read the
preference cookie. Each exported page carries a tiny bootstrap script that picks
the matching variant before first paint, so there is no flash of the wrong
theme.

Not exported (needs a server): booking POSTs, enquiries, /saved/ (device only
already), /search/, the admin and the legacy CMS.
"""
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

# Pages exported in both themes and both languages.
BILINGUAL_THEMED = [
    ('/', 'index.html'),
    ('/projects/', 'projects/index.html'),
    ('/services/', 'services/index.html'),
    ('/about/', 'about/index.html'),
    ('/booking/', 'booking/index.html'),
    ('/contact/', 'contact/index.html'),
    ('/gallery/', 'gallery/index.html'),
    ('/news/', 'news/index.html'),
    ('/faq/', 'faq/index.html'),
    ('/investors/', 'investors/index.html'),
    ('/suburbs/', 'suburbs/index.html'),
    ('/land-sharing/', 'land-sharing/index.html'),
    ('/projects/compare/', 'projects/compare/index.html'),
    ('/saved/', 'saved/index.html'),
]

# Detail routes are discovered from the database.
DETAIL_PREFIXES = [
    ('/projects/{}/', 'projects/{}/index.html'),
    ('/projects/{}/unit/{}/', 'projects/{}/unit/{}/index.html'),
    ('/suburbs/{}/', 'suburbs/{}/index.html'),
    ('/services/{}/', 'services/{}/index.html'),
    ('/news/{}/', 'news/{}/index.html'),
]

THEMES = ('light', 'dark')
LANGS = ('en', 'bn')


def _slugify_path(path):
    """Turn /a/b/ into the file that should hold it on disk."""
    clean = path.strip('/')
    return 'index.html' if not clean else clean + '/index.html'


class Command(BaseCommand):
    help = 'Export the public site to static HTML (for GitHub Pages).'

    def add_arguments(self, parser):
        parser.add_argument('--out', default='dist', help='Output directory.')
        parser.add_argument('--base-path', default='/',
                            help='Public path prefix, e.g. /stibuilders/ for a project page.')

    def handle(self, *args, **opts):
        out = Path(opts['out']).resolve()
        base_path = opts['base_path']
        if not base_path.endswith('/'):
            base_path += '/'

        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)

        self.client = Client()
        self.base_path = base_path
        self.written = []

        # ---- discover detail routes -------------------------------------
        routes = [r for r, _ in BILINGUAL_THEMED]
        for prefix, _ in DETAIL_PREFIXES:
            for slugs in self._slugs(prefix):
                if not isinstance(slugs, tuple):
                    slugs = (slugs,)
                routes.append(prefix.format(*slugs))

        # ---- render every page, every theme, every language -------------
        rendered = 0
        for route in routes:
            for theme in THEMES:
                for lang in LANGS:
                    html = self._render(route, theme, lang)
                    if html is None:
                        continue
                    self._write_variant(out, route, theme, lang, html)
                    rendered += 1

        # ---- index.html shims + base variants ---------------------------
        for route in routes:
            self._write_router(out, route)

        # ---- assets -----------------------------------------------------
        self._copy_assets(out)

        # ---- auto-repair: export any route that something links to ------
        for _ in range(3):
            missing = self._missing_routes(out, routes)
            if not missing:
                break
            for route in missing:
                routes.append(route)
                for theme in THEMES:
                    for lang in LANGS:
                        html = self._render(route, theme, lang)
                        if html is not None:
                            self._write_variant(out, route, theme, lang, html)
                self._write_router(out, route)
            self.stdout.write(f'  exported {len(missing)} route(s) found by the link check')
            # rebind choices rendered inside the newly exported pages
            for route in missing:
                self._bind_choices(out, route)

        # ---- validate ----------------------------------------------------
        broken = self._check_links(out, routes)

        # ---- extras -----------------------------------------------------
        self._write_404(out)
        self._write_nojekyll(out)
        self._write_redirects(out, routes)

        if broken:
            self.stdout.write(self.style.WARNING(
                f'{len(broken)} internal link(s) have no exported target:'))
            for b in sorted(broken)[:15]:
                self.stdout.write('   ' + b)
        else:
            self.stdout.write('  link check: every internal link resolves')

        self.stdout.write(self.style.SUCCESS(
            f'Exported {len(routes)} routes x {len(THEMES)} themes x {len(LANGS)} langs '
            f'= {rendered} pages into {out}'))

    # ------------------------------------------------------------------
    def _slugs(self, prefix):
        """Slugs to expand a detail-route template. Unit pages are nested, so
        they are returned already prepared as (project_slug, unit_pk) pairs."""
        from website import models as m
        if prefix == '/projects/{}/unit/{}/':
            return list(m.Apartment.objects
                        .filter(is_active=True)
                        .select_related('project')
                        .values_list('project__slug', 'pk'))
        mapping = {
            '/projects/{}/': m.Project,
            '/suburbs/{}/': m.Location,
            '/services/{}/': m.Service,
            '/news/{}/': m.NewsPost,
        }
        model = mapping[prefix]
        return list(model.objects.values_list('slug', flat=True))

    def _render(self, route, theme, lang):
        self.client.cookies['sti_theme'] = theme
        self.client.cookies['sti_lang'] = lang
        res = self.client.get(route)
        if res.status_code != 200:
            self.stderr.write(f'  skip {route} ({res.status_code})')
            return None
        return self._rewrite(res.content.decode('utf-8'))

    def _rewrite(self, html):
        """Make absolute URLs relative so the export works under any prefix."""
        base = self.base_path.rstrip('/')

        def strip_prefix(m):
            url = m.group(1)
            if url.startswith(base + '/'):
                return 'url({}('.format(base)  # keep absolute for CSS url() refs
            return m.group(0)

        # 1. root-relative links and assets -> relative, keeping the prefix
        def rel(m):
            quote, url = m.group(1), m.group(2)
            if url.startswith(('//', 'http://', 'https://', 'mailto:', 'tel:', '#', 'data:')):
                return m.group(0)
            if not url.startswith('/'):
                return m.group(0)
            return '{}={}{}{}'.format(m.group(0).split('=')[0], quote, base + url, quote)

        html = re.sub(r'(href|src|action)=(["\'])(/[^"\']*)\2',
                      lambda m: '{}={}{}{}'.format(
                          m.group(1), m.group(2),
                          base + m.group(3) if not m.group(3).startswith('//') else m.group(3),
                          m.group(2)),
                      html)
        # 2. URLs that live inside JSON (the map payload) and inline styles are
        #    not attributes, so the pass above misses them; the client builds an
        #    <img src> from them at runtime and would hit the server root.
        for kind in ('media', 'static'):
            marker = '__ALREADY_PREFIXED_' + kind + '__'
            html = html.replace(f'"{base}/{kind}/', marker)
            html = html.replace(f'"/{kind}/', f'"{base}/{kind}/')
            html = html.replace(marker, f'"{base}/{kind}/')
        html = html.replace('url(/static/', 'url({}/static/'.format(base))
        # 3. absolute site origin
        html = re.sub(r'https?://(127\.0\.0\.1|localhost)(:\d+)?', '', html)
        return html

    def _rewrite_lang_links(self, html, theme, lang):
        """Point the EN/BN switcher at a sibling file instead of /prefs/.

        /prefs/ is a server route that sets a cookie; on a static host it would
        404 out to a page that does not exist inside the export.
        """
        def repl(m):
            want = m.group(1)
            # absolute path: variant files live next to the shim, and an
            # absolute href survives any depth without <base> games
            return 'href="{}/{}-{}.html" data-pref="lang"'.format(
                self.base_path.rstrip('/'), theme, want)

        html = re.sub(r'href="[^"]*/prefs/\?lang=(en|bn)[^"]*" data-pref="lang"', repl, html)
        # the active state must reflect this variant
        html = html.replace('class="pref-btn is-active"', 'class="pref-btn"')
        return html

    def _write_variant(self, out, route, theme, lang, html):
        html = self._rewrite_lang_links(html, theme, lang)
        target = out / _slugify_path(route)
        target.parent.mkdir(parents=True, exist_ok=True)
        variant = target.with_name(f'{theme}-{lang}.html')
        variant.write_text(html, encoding='utf-8')
        self.written.append(variant)

    def _write_router(self, out, route):
        """Write the real index.html: a shim that picks a theme/lang variant."""
        target = out / _slugify_path(route)
        target.parent.mkdir(parents=True, exist_ok=True)
        depth = len(target.relative_to(out).parts) - 1
        # variants sit next to the shim unless this is the root page
        if route == '/':
            # /dist/index.html routes to index-light-en.html etc.
            shim = self._shim_code('', depth)
        else:
            shim = self._shim_code('', depth)
        target.write_text(shim, encoding='utf-8')

    def _shim_code(self, _unused, depth):
        return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Loading…</title>
<script>
/* Static export: pick the page variant matching the visitor's saved
   theme and language before anything paints, then replace this document.
   There is no server here, so localStorage is the source of truth. */
(function () {
  function read(key, allowed, fallback) {
    var value = null;
    try { value = localStorage.getItem(key); } catch (e) {}
    return allowed.indexOf(value) >= 0 ? value : fallback;
  }
  /* language: saved choice, else the browser's preference */
  var lang = null;
  try { lang = localStorage.getItem('sti_lang'); } catch (e) {}
  if (lang !== 'en' && lang !== 'bn') {
    lang = (navigator.language || 'en').toLowerCase().indexOf('bn') === 0 ? 'bn' : 'en';
  }
  var theme = read('sti_theme', ['light', 'dark'], 'light');
  location.replace(theme + '-' + lang + '.html');
})();
</script>
<noscript><meta http-equiv="refresh" content="0; url=light-en.html"></noscript>
</head>
<body></body>
</html>
"""

    # ------------------------------------------------------------------
    def _copy_assets(self, out):
        """Copy static files, then add per-page theme/lang overrides."""
        src = Path(settings.STATIC_ROOT) if Path(settings.STATIC_ROOT).exists() else None
        if src is None:
            from django.contrib.staticfiles import finders
            src = Path(finders.find('website').replace('website', '').rstrip('/'))
        dest = out / 'static'
        if dest.exists():
            shutil.rmtree(dest)
        # Only the assets the public site actually references are copied: the
        # legacy realstateapp/ckeditor/admin bundles are ~145 MB and none of
        # them are used by the exported pages (they would also blow past the
        # GitHub Pages artifact size limit).
        exported = {path.name for path in out.rglob('*.html')}
        referenced = set()
        for page in out.rglob('*.html'):
            try:
                text = page.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            for url in re.findall(r'(?:href|src)="(/[^"?#]*\.(?:css|js|png|jpe?g|svg|webp|woff2?|ttf))"', text):
                referenced.add(url.lstrip('/'))

        static_files = Path(settings.STATIC_ROOT)
        if not static_files.exists():
            from django.core.management import call_command
            call_command('collectstatic', verbosity=0, interactive=False,
                         clear=True, stdout=open(os.devnull, 'w'))
        for rel in referenced:
            rel = rel.split('/static/', 1)[-1] if '/static/' in rel else rel.replace('static/', '', 1)
            src_file = static_files / rel
            if src_file.exists() and src_file.is_file():
                target = dest / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, target)
        # keep the whole website app bundle: fonts and icons are pulled in by CSS
        app_static = static_files / 'website'
        if app_static.exists():
            shutil.copytree(app_static, dest / 'website', dirs_exist_ok=True)
        # uploaded media
        media_root = Path(settings.MEDIA_ROOT)
        if media_root.exists():
            shutil.copytree(media_root, out / 'media', dirs_exist_ok=True)
        self.stdout.write(f'  assets -> {dest}')
        self._write_overrides(dest)

    def _write_overrides(self, static_dir):
        """Create the theme/lang CSS and JS overlays referenced by the exporter."""
        css = static_dir / 'website' / 'css'
        js = static_dir / 'website' / 'js'
        css.mkdir(parents=True, exist_ok=True)
        js.mkdir(parents=True, exist_ok=True)

        (js / 'static-export.js').write_text(STATIC_EXPORT_JS, encoding='utf-8')
        (css / 'static-export.css').write_text(STATIC_EXPORT_CSS, encoding='utf-8')

    def _bind_choices(self, out, route):
        """Selects and tabs in a static page must carry their default selection.

        Without a server the browser picks the first option, which would show
        the wrong value (e.g. "Any availability" instead of the page you landed
        on). Binding happens at write time so no JS is needed.
        """
        import html as html_mod
        target = out / _slugify_path(route)
        for theme in THEMES:
            for lang in LANGS:
                variant = target.with_name(f'{theme}-{lang}.html')
                if not variant.exists():
                    continue
                text = variant.read_text(encoding='utf-8')

                def bind_option(m):
                    tag = m.group(0)
                    if html_mod.escape(m.group(2)) in (html_mod.escape(route), route):
                        if 'selected' not in tag:
                            return tag.replace('<option', '<option selected', 1)
                    return tag

                text = re.sub(r'<option[^>]*value="([^"]*)"[^>]*>', bind_option, text)
                variant.write_text(text, encoding='utf-8')

    def _missing_routes(self, out, routes):
        """Routes referenced by links in the export that we have not written yet."""
        import html as html_mod
        base = self.base_path.rstrip('/')
        missing = set()
        skip = ('/static/', '/media/', '/prefs/', '/search/',
                '/booking/', '/admin/', '/cms/', '/property/', '.json', '.xml')
        for html_file in out.rglob('*.html'):
            try:
                text = html_file.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            for url in re.findall(r'(?:href|action)="(/[^"#?]*)"', text):
                if not url.startswith(base + '/'):
                    continue
                route = url[len(base):]
                if any(s in route for s in skip):
                    continue
                if re.search(r'/(light|dark)-(en|bn)\.html$', route):
                    continue  # variant file produced by the lang-link rewrite
                if route in routes:
                    continue
                target = out / _slugify_path(route)
                if target.exists():
                    continue
                missing.add(route)
        return sorted(missing)

    def _check_links(self, out, routes):
        """Every href/src in the export must point at a file we actually wrote."""
        known = set()
        for path in out.rglob('*'):
            if path.is_file():
                known.add('/' + str(path.relative_to(out)))
        broken = set()
        base = self.base_path.rstrip('/')
        for html_file in out.rglob('*.html'):
            try:
                html = html_file.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                continue
            for url in re.findall(r'(?:href|src)="(/[^"#?]*)"', html):
                if not url.startswith(base + '/'):
                    continue
                local = url[len(base):]
                if not local or local.endswith('/'):
                    local += 'index.html'
                if local not in known:
                    broken.add(f'{url}  (from /{html_file.relative_to(out)})')
        return broken

    # ------------------------------------------------------------------
    def _write_404(self, out):
        (out / '404.html').write_text(
            '<!doctype html><meta charset="utf-8">'
            '<title>Page not found</title>'
            '<meta http-equiv="refresh" content="0; url=./">'
            '<p>Page not found. <a href="./">Return to the homepage</a>.</p>',
            encoding='utf-8')

    def _write_nojekyll(self, out):
        (out / '.nojekyll').write_text('', encoding='utf-8')

    def _write_redirects(self, out, routes):
        """Legacy URLs that used to 301 on the server become redirect pages."""
        legacy = {
            'browse-all-property': 'projects/',
            'property-search': 'projects/',
            'search-result': 'projects/',
            'about-us': 'about/',
            'contact-us': 'contact/',
            'client-testimonial': 'about/',
            'privacy-policy': 'faq/',
            'terms-conditions': 'faq/',
            'frequently-question': 'faq/',
        }
        for old, new in legacy.items():
            target = out / old / 'index.html'
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                '<!doctype html><meta charset="utf-8">'
                f'<title>Redirecting…</title>'
                f'<link rel="canonical" href="../{new}">'
                f'<meta http-equiv="refresh" content="0; url=../{new}">'
                f'<p>This page has moved. <a href="../{new}">Continue</a>.</p>',
                encoding='utf-8')


STATIC_EXPORT_JS = r"""/* GitHub Pages build: there is no server to read the preference cookie, so
   theme and language live in localStorage here. */
(function () {
  var root = document.documentElement;
  var THEME_KEY = 'sti_theme', LANG_KEY = 'sti_lang';
  function store(key, value) { try { localStorage.setItem(key, value); } catch (e) {} }
  function read(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }

  /* preferences picked on one page have to survive the next navigation */
  document.addEventListener('click', function (e) {
    var theme = e.target.closest('[data-theme-toggle], #themeToggle');
    if (theme) {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      store(THEME_KEY, next);
      return;
    }
    var lang = e.target.closest('[data-pref="lang"]');
    if (lang && lang.dataset.value) store(LANG_KEY, lang.dataset.value);
  }, true);

  /* keep the visible label in sync when the overshell swapped the document */
  var theme = root.getAttribute('data-theme');
  var dark = theme === 'dark';
  var labels = document.querySelectorAll('[data-theme-label]');
  for (var i = 0; i < labels.length; i++) {
    labels[i].textContent = dark ? 'Light mode' : 'Dark mode';
  }
})();
"""

STATIC_EXPORT_CSS = """/* GitHub Pages build: extra rules that only apply to the static export. */
.share-hint { display: none; }
"""
