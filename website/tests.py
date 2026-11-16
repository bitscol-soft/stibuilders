"""Smoke + behaviour tests for the redesigned STI Builders website.

Run with:  python manage.py test website
"""
import datetime as dt

from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from .context_processors import LANG_COOKIE, THEME_COOKIE
from .models import (Amenity, Apartment, Booking, Enquiry, Feature, Landmark, Location,
                     Milestone, Project, SiteSetting, short_bdt)


class WebsiteSmokeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SiteSetting.objects.create(company_name='STI Builders Limited', phone='01923505050',
                                   email='info@example.com')
        cls.location = Location.objects.create(
            name='Uttara', zone='North Dhaka', latitude=23.8759, longitude=90.3795,
            avg_price_per_sqft=9200, price_growth_yoy=7.4, demand_index=88, livability_score=84)
        Landmark.objects.create(location=cls.location, name='Metro Station 3',
                                category='metro', distance_km=0.9, drive_minutes=4)
        cls.amenity = Amenity.objects.create(name='Swimming Pool', icon='pool')
        cls.feature = Feature.objects.create(name='Imported tiles')
        today = timezone.now().date()
        cls.project = Project.objects.create(
            name='Test Tower', location=cls.location, stage='ongoing', category='residential',
            price_from=15000000, price_per_sqft=8500, size_from=1500, size_to=2000,
            beds_from=3, beds_to=4, total_units=30, floors=12, land_area=7, handover_date=today,
            completion_pct=55, featured=True, map_latitude=23.8749, map_longitude=90.3792)
        cls.project.amenities.add(cls.amenity)
        cls.project.features.add(cls.feature)
        Milestone.objects.create(project=cls.project, title='Piling', is_done=True, progress_pct=100)
        Milestone.objects.create(project=cls.project, title='Structure', progress_pct=40,
                                 target_date=today + dt.timedelta(days=90))
        cls.unit = Apartment.objects.create(project=cls.project, unit_no='A1', unit_type='3bed',
                                            title='Type A', size_sft=1500, beds=3, baths=3,
                                            price=15000000, status='available')

    # -- pages ----------------------------------------------------------
    def test_home_renders(self):
        res = self.client.get(reverse('website:home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Test Tower')

    def test_project_list_and_filters(self):
        url = reverse('website:project_list')
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.get(url, {'stage': 'ongoing'}).status_code, 200)
        self.assertEqual(self.client.get(url, {'stage': 'upcoming'}).status_code, 200)
        self.assertEqual(self.client.get(url, {'beds': '3', 'price_min': '1000000'}).status_code, 200)
        self.assertEqual(self.client.get(url, {'amenity': [self.amenity.pk]}).status_code, 200)

    def test_filter_excludes_other_stages(self):
        url = reverse('website:project_list')
        self.assertEqual(self.client.get(url, {'stage': 'ongoing'}).context['total_found'], 1)
        self.assertEqual(self.client.get(url, {'stage': 'upcoming'}).context['total_found'], 0)

    def test_project_detail_sections(self):
        res = self.client.get(self.project.get_absolute_url())
        self.assertEqual(res.status_code, 200)
        for anchor in ('id="overview"', 'id="building"', 'id="apartments"', 'id="amenities"',
                       'id="location"', 'id="design"', 'id="milestones"', 'id="landshare"',
                       'id="videos"', 'id="profile"', 'id="social"'):
            self.assertContains(res, anchor)

    def test_suburb_pages(self):
        self.assertEqual(self.client.get(reverse('website:suburb_list')).status_code, 200)
        self.assertEqual(self.client.get(self.location.get_absolute_url()).status_code, 200)

    def test_static_pages(self):
        for name in ('about', 'services', 'land_sharing', 'investors', 'news', 'gallery',
                     'contact', 'faq', 'booking', 'saved', 'compare', 'search'):
            with self.subTest(page=name):
                self.assertEqual(self.client.get(reverse(f'website:{name}')).status_code, 200)

    def test_map_and_units_json(self):
        res = self.client.get(reverse('website:project_map_data'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()['projects']), 1)
        res = self.client.get(reverse('website:units_json', args=[self.project.slug]))
        self.assertEqual(res.json()['units'][0]['label'], 'Type A')

    def test_icons_render_as_svg_not_escaped_text(self):
        """Icons must be real <svg><use> markup pointing at the shared sprite.

        The sprite lives in one cached file (website/img/icons.svg) rather than
        being inlined into every page: it was 24 KB repeated on all 400+
        exported pages.
        """
        import re
        from pathlib import Path
        from django.conf import settings

        res = self.client.get(reverse('website:home'))
        html = res.content.decode()
        self.assertNotIn('&lt;svg', html)
        self.assertNotIn('&lt;use', html)
        self.assertIn('<use href="/static/website/img/icons.svg#i-', html)

        sprite = (Path(settings.BASE_DIR) / 'website' / 'static' / 'website'
                  / 'img' / 'icons.svg').read_text(encoding='utf-8')
        defined = set(re.findall(r'<symbol id="([^"]+)"', sprite))
        self.assertGreater(len(defined), 50, 'sprite looks empty')
        referenced = set(re.findall(r'icons\.svg#([^"]+)"', html))
        missing = referenced - defined
        self.assertEqual(missing, set(), f'icons referenced but not in sprite: {missing}')

    def test_sitemap_and_robots(self):
        self.assertEqual(self.client.get('/sitemap.xml').status_code, 200)
        self.assertEqual(self.client.get('/robots.txt').status_code, 200)

    def test_404_page(self):
        res = self.client.get('/projects/does-not-exist/')
        self.assertEqual(res.status_code, 404)

    # -- interactions ----------------------------------------------------
    def test_booking_creates_request(self):
        res = self.client.post(reverse('website:booking'), {
            'project': self.project.pk, 'apartment': self.unit.pk, 'kind': 'visit',
            'full_name': 'Rifat', 'phone': '01711000000', 'preferred_time': '11:00 AM',
        })
        self.assertEqual(res.status_code, 302)
        booking = Booking.objects.get()
        self.assertTrue(booking.reference.startswith('STI-'))
        self.assertEqual(booking.project, self.project)

    def test_booking_ignores_invalid_project(self):
        res = self.client.post(reverse('website:booking'), {
            'project': '999999', 'full_name': 'X', 'phone': '017', 'kind': 'nonsense'})
        self.assertEqual(res.status_code, 302)
        self.assertIsNone(Booking.objects.get().project)

    def test_enquiry_creates_record(self):
        res = self.client.post(reverse('website:contact'), {
            'name': 'Nusrat', 'phone': '017', 'subject': 'land', 'message': 'hello'})
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Enquiry.objects.count(), 1)

    def test_save_toggle(self):
        url = reverse('website:save_project')
        self.assertTrue(self.client.post(url, {'slug': self.project.slug}).json()['saved'])
        self.assertFalse(self.client.post(url, {'slug': self.project.slug}).json()['saved'])

    def test_language_switch_swaps_ui_strings(self):
        res = self.client.get(reverse('website:home'), HTTP_COOKIE='sti_lang=bn')
        html = res.content.decode()
        self.assertIn('lang="bn"', html)
        self.assertIn('প্রকল্প', html)          # Projects
        self.assertIn('ভিজিট বুক করুন', html)     # Book a visit
        # English must come back when the cookie says so
        res_en = self.client.get(reverse('website:home'), HTTP_COOKIE='sti_lang=en')
        self.assertIn('lang="en"', res_en.content.decode())

    def test_theme_switch_sets_attribute(self):
        res = self.client.get(reverse('website:home'), HTTP_COOKIE='sti_theme=dark')
        self.assertIn('data-theme="dark"', res.content.decode())
        res = self.client.get(reverse('website:home'), HTTP_COOKIE='sti_theme=light')
        self.assertIn('data-theme="light"', res.content.decode())

    def test_set_prefs_cookie_and_redirect(self):
        res = self.client.get(reverse('website:set_prefs'), {'lang': 'bn', 'next': '/projects/'})
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res['Location'], '/projects/')
        self.assertEqual(res.cookies['sti_lang'].value, 'bn')

    def test_set_prefs_rejects_offsite_next(self):
        res = self.client.get(reverse('website:set_prefs'), {'lang': 'bn', 'next': 'https://evil.example/'})
        self.assertEqual(res['Location'], '/')

    def test_public_pages_can_be_framed_for_the_preview(self):
        # The hosted preview embeds the app in a cross-origin iframe, so public
        # pages must not carry X-Frame-Options.
        for url in (reverse('website:home'), reverse('website:project_list'),
                    reverse('website:booking')):
            with self.subTest(url=url):
                res = self.client.get(url)
                self.assertNotIn('X-Frame-Options', res.headers)
                csp = res.headers.get('Content-Security-Policy', '')
                self.assertIn('frame-ancestors', csp)
                # An http parent origin must be allowed too, otherwise local and
                # non-TLS previews get ERR_BLOCKED_BY_RESPONSE.
                self.assertNotIn('https:', csp)
                self.assertIn('*', csp)

    def test_admin_keeps_clickjacking_protection(self):
        res = self.client.get('/admin/login/')
        self.assertEqual(res.headers.get('X-Frame-Options'), 'SAMEORIGIN')

    def test_footer_uses_dark_image_band(self):
        res = self.client.get(reverse('website:home'))
        self.assertContains(res, 'site-footer has-image')
        self.assertContains(res, 'footer-city.jpg')

    def test_legacy_redirects(self):
        res = self.client.get('/browse-all-property/')
        self.assertEqual(res.status_code, 301)
        self.assertEqual(res['Location'], '/projects/')


class MoneyFormatTests(TestCase):
    def test_bengali_grouping(self):
        self.assertEqual(short_bdt(15000000), '৳ 1.50 Cr')
        self.assertEqual(short_bdt(7800000), '৳ 78.0 Lac')
        self.assertEqual(short_bdt(None), 'On request')

    def test_full_grouping(self):
        from website.models import money
        self.assertEqual(money(12500000), '1,25,00,000')
        self.assertEqual(money(999), '999')


class PreferencePersistenceTests(TestCase):
    """The theme and language toggles must survive inside the preview iframe.

    Browsers drop SameSite=Lax cookies on cross-site iframe requests, which made
    both toggles appear broken even though the click handler ran. The cookies
    therefore have to be SameSite=None over HTTPS.
    """

    def test_theme_cookie_is_iframe_safe(self):
        res = self.client.get('/prefs/', {'theme': 'dark', 'next': '/'})
        self.assertEqual(res.status_code, 302)
        cookie = res.cookies[THEME_COOKIE]
        self.assertEqual(cookie.value, 'dark')
        self.assertEqual(cookie['samesite'].lower(), 'none')
        self.assertTrue(cookie['secure'])

    def test_language_cookie_is_iframe_safe(self):
        res = self.client.get('/prefs/', {'lang': 'bn', 'next': '/'})
        self.assertEqual(res.status_code, 302)
        cookie = res.cookies[LANG_COOKIE]
        self.assertEqual(cookie.value, 'bn')
        self.assertEqual(cookie['samesite'].lower(), 'none')
        self.assertTrue(cookie['secure'])

    def test_preferences_render_server_side(self):
        client = Client()
        client.cookies[THEME_COOKIE] = 'dark'
        client.cookies[LANG_COOKIE] = 'bn'
        res = client.get(reverse('website:project_list'))
        self.assertContains(res, 'data-theme="dark"')
        self.assertContains(res, 'lang="bn"')

    def test_bad_preference_values_are_ignored(self):
        res = self.client.get('/prefs/', {'theme': 'neon', 'lang': 'fr', 'next': '/'})
        self.assertEqual(res.status_code, 302)
        self.assertNotIn(THEME_COOKIE, res.cookies)
        self.assertNotIn(LANG_COOKIE, res.cookies)


class IconSizingTests(TestCase):
    """An <svg> with no width/height and no CSS renders at 300x150.

    That is exactly what made icons and buttons look enormous when the
    stylesheet was missing or still loading, so every icon carries hard
    fallback attributes.
    """

    def test_icons_carry_fallback_dimensions(self):
        res = self.client.get(reverse('website:home'))
        self.assertEqual(res.status_code, 200)
        html = res.content.decode()
        self.assertNotIn('<svg class="ico-svg " aria-hidden', html)
        self.assertIn('width="18" height="18"', html)


class BannerCoverageTests(TestCase):
    """Every interior page must carry the shared title banner.

    Banners used to be hand-rolled per template, so some pages had a photo and
    most had none. They now come from one tag, and this keeps it that way.
    """

    BANNER_PAGES = [
        'website:project_list', 'website:services', 'website:about',
        'website:gallery', 'website:news', 'website:contact', 'website:faq',
        'website:booking', 'website:investors', 'website:suburb_list',
        'website:land_sharing', 'website:compare', 'website:saved',
    ]

    def test_every_interior_page_has_a_banner_image(self):
        for name in self.BANNER_PAGES:
            with self.subTest(page=name):
                res = self.client.get(reverse(name))
                self.assertEqual(res.status_code, 200)
                html = res.content.decode()
                self.assertIn('page-hero', html, f'{name} has no banner')
                self.assertRegex(
                    html, r'<section class="page-hero[^"]*">\s*<img src="[^"]+\.(jpg|jpeg|png)"',
                    f'{name} banner has no image')


class FooterConflictTests(TestCase):
    """The footer must not repeat the call-to-action band.

    home/about/services/land-sharing/suburbs already render a .cta-band above
    the footer. A second one inside the footer made "Next step / Come and see
    the site" appear twice, which read as two overlapping sections.
    """

    def test_footer_does_not_repeat_the_cta_band(self):
        res = self.client.get(reverse('website:home'))
        html = res.content.decode()
        self.assertEqual(html.count('Come see a site before you decide'), 1)
        self.assertEqual(html.count('Come and see the site before you decide'), 0)
        self.assertEqual(html.count('site-footer__cta'), 0)

    def test_footer_image_is_present_and_not_lazy(self):
        res = self.client.get(reverse('website:home'))
        html = res.content.decode()
        self.assertIn('footer-city.jpg', html)
        # a lazy background can stay blank on tall footers that never scroll
        self.assertNotRegex(html, r'footer-city\.jpg[^>]*loading="lazy"')


class StaticExportTests(TestCase):
    """The GitHub Pages build is part of the deliverable, so it is tested."""

    def test_export_produces_theme_and_language_variants(self):
        import tempfile
        from pathlib import Path
        from django.core.management import call_command

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'dist'
            call_command('export_static', out=str(out), base_path='/stibuilders/',
                         verbosity=0)
            # the router plus one file per theme/language combination
            self.assertTrue((out / 'index.html').exists())
            for theme in ('light', 'dark'):
                for lang in ('en', 'bn'):
                    self.assertTrue(
                        (out / f'{theme}-{lang}.html').exists(),
                        f'missing {theme}-{lang}.html')
            router = (out / 'index.html').read_text()
            self.assertIn('location.replace', router)
            # assets are rewritten under the repo prefix
            page = (out / 'light-en.html').read_text()
            self.assertIn('/stibuilders/static/', page)
            self.assertNotIn('"/media/', page)

    def test_export_has_no_unresolved_internal_links(self):
        import io
        import tempfile
        from pathlib import Path
        from django.core.management import call_command

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'dist'
            buf = io.StringIO()
            call_command('export_static', out=str(out), base_path='/stibuilders/',
                         stdout=buf, verbosity=0)
            self.assertIn('every internal link resolves', buf.getvalue())


class ApartmentDetailTests(TestCase):
    """Every flat gets its own page, not just a modal fragment."""

    @classmethod
    def setUpTestData(cls):
        from django.core.management import call_command
        call_command('seed_website', verbosity=0)

    def _unit(self, **filters):
        from website.models import Apartment
        qs = Apartment.objects.filter(is_active=True).select_related('project')
        return qs.filter(**filters).first() or qs.first()

    def test_unit_page_renders_with_its_own_url(self):
        unit = self._unit()
        res = self.client.get(reverse('website:apartment_detail',
                                      args=[unit.project.slug, unit.pk]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, unit.size_label)
        self.assertEqual(res.context['unit'].pk, unit.pk)

    def test_unit_page_is_reachable_from_the_project_page(self):
        unit = self._unit()
        res = self.client.get(reverse('website:project_detail',
                                      args=[unit.project.slug]))
        expected = reverse('website:apartment_detail', args=[unit.project.slug, unit.pk])
        self.assertContains(res, expected)

    def test_unit_page_covers_the_required_detail(self):
        unit = self._unit()
        html = self.client.get(reverse('website:apartment_detail',
                                       args=[unit.project.slug, unit.pk])).content.decode()
        for section in ('id="overview"', 'id="plan"', 'id="spaces"', 'id="finishing"',
                        'id="payment"', 'id="building"', 'id="location"'):
            self.assertIn(section, html, f'missing {section}')
        # beds, baths, size and features must all be visible text
        self.assertIn(str(unit.beds), html)
        self.assertIn(str(unit.baths), html)

    def test_payment_schedule_sums_to_the_flat_price(self):
        unit = self._unit(price__isnull=False)
        schedule = unit.pricing
        self.assertTrue(schedule)
        self.assertEqual(sum(row['pct'] for row in schedule), 100)
        self.assertEqual(sum(row['amount'] for row in schedule), int(unit.price))

    def test_schedule_falls_back_to_the_project_entry_price(self):
        from website.models import Apartment
        unit = (Apartment.objects.filter(price__isnull=True,
                                         project__price_from__isnull=False)
                .select_related('project').first())
        if unit is None:
            self.skipTest('no unpriced unit with a project entry price')
        self.assertTrue(unit.pricing_is_projected)
        self.assertEqual(sum(r['amount'] for r in unit.pricing), int(unit.project.price_from))

    def test_unknown_unit_is_404(self):
        res = self.client.get(reverse('website:apartment_detail',
                                      args=['sti-royal-tower', 999999]))
        self.assertEqual(res.status_code, 404)

    def test_unit_from_another_project_is_404(self):
        from website.models import Apartment
        unit = self._unit()
        other = Apartment.objects.exclude(project=unit.project).first()
        if other is None:
            self.skipTest('only one project seeded')
        res = self.client.get(reverse('website:apartment_detail',
                                      args=[other.project.slug, unit.pk]))
        self.assertEqual(res.status_code, 404)


class HeaderPreferenceControlTests(TestCase):
    """Both preference controls must stay usable at every width.

    The language switch used to be display:none below 860px, so the site
    silently lost its EN/BN toggle on phones and in narrow windows.
    """

    def test_language_switch_is_not_hidden_by_css(self):
        import re
        from pathlib import Path
        from django.conf import settings
        css = (Path(settings.BASE_DIR) / 'website' / 'static' / 'website'
               / 'css' / 'sti.css').read_text(encoding='utf-8')
        # find any rule that hides the header pref-group
        for block in re.findall(r'\.nav-tools[^{]*\{[^}]*\}', css):
            self.assertNotIn('pref-group', block.replace(' ', ''), 
                             'a header rule still hides the language switch')

    def test_both_controls_render_on_every_page(self):
        for name in ('website:home', 'website:project_list', 'website:about'):
            html = self.client.get(reverse(name)).content.decode()
            self.assertIn('data-pref="lang"', html, f'{name} has no language switch')
            self.assertRegex(html, r'id="themeToggle"', f'{name} has no theme switch')

    def test_sticky_bars_use_theme_tokens(self):
        """A hard-coded cream background made dark-mode links invisible."""
        import re
        from pathlib import Path
        from django.conf import settings
        css = (Path(settings.BASE_DIR) / 'website' / 'static' / 'website'
               / 'css' / 'sti.css').read_text(encoding='utf-8')
        for selector in ('.pd-subnav', '.site-header.is-solid'):
            block = re.search(re.escape(selector) + r'[^{]*\{[^}]*\}', css)
            self.assertIsNotNone(block, f'{selector} rule missing')
            self.assertNotIn('rgba(251,249,245', block.group(0),
                             f'{selector} hard-codes a light background')


class BengaliCoverageTests(TestCase):
    """No key should survive as English when the UI is in Bengali.

    A key added to a template without a matching entry in i18n_bn falls back to
    the English default, which is how the apartment page shipped half-English.
    """

    PAGES = ['website:home', 'website:project_list', 'website:about',
             'website:faq', 'website:booking', 'website:apartment_detail']

    def test_apartment_and_footer_keys_exist(self):
        from website.i18n_bn import BN
        for key in ('unit.overview', 'unit.plan', 'unit.spaces', 'unit.finishing',
                    'unit.payment', 'unit.building', 'unit.location', 'unit.reserve',
                    'unit.price', 'unit.booking', 'ft.eyebrow', 'ft.headline',
                    'ft.hotline', 'ft.language', 'room.living', 'room.kitchen'):
            self.assertIn(key, BN, f'missing Bengali string for {key}')
            self.assertTrue(BN[key].strip(), f'empty Bengali string for {key}')

    def test_template_keys_are_all_translated(self):
        import re
        from pathlib import Path
        from django.conf import settings
        from website.i18n_bn import BN
        templates = (Path(settings.BASE_DIR) / 'website' / 'templates')
        missing = set()
        for path in templates.rglob('*.html'):
            text = path.read_text(encoding='utf-8')
            for key in re.findall(r"{%\s*t\s+'([^']+)'", text):
                if key not in BN:
                    missing.add(key)
        self.assertEqual(missing, set(), f'untranslated keys: {sorted(missing)}')
