"""Template helpers for the STI Builders website."""
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from website import models as m
from website.i18n_bn import BN, BN_DIGITS

register = template.Library()

ICON_ALIASES = {
    'fire fighting': 'i-fire', 'fire': 'i-fire', 'parking': 'i-car', 'car': 'i-car',
    'community support': 'i-users', 'users': 'i-users', 'power sub-station': 'i-power',
    'power': 'i-power', 'inter-communication': 'i-intercom', 'intercom': 'i-intercom',
    'near university': 'i-school', 'school': 'i-school', 'pool': 'i-pool', 'gym': 'i-gym',
    'security': 'i-security', 'cctv': 'i-cctv', 'generator': 'i-generator', 'wifi': 'i-wifi',
    'mosque': 'i-mosque', 'garden': 'i-garden', 'tree': 'i-tree', 'water': 'i-water',
    'roof': 'i-roof', 'lounge': 'i-lounge', 'play': 'i-playground', 'club': 'i-club',
    'laundry': 'i-laundry', 'ev': 'i-ev', 'lift': 'i-lift', 'stairs': 'i-stairs',
    'hospital': 'i-hospital', 'mall': 'i-mall', 'park': 'i-park', 'metro': 'i-metro',
    'airport': 'i-airport', 'office': 'i-office', 'other': 'i-map-pin',
}


@register.simple_tag
def icon(name, cls=''):
    """Render an inline SVG reference to the sprite defined in _icons.html.

    The markup is marked safe so Django does not escape it; the values are
    interpolated through format_html, which escapes ``cls`` for us.
    """
    key = (name or '').strip().lower()
    symbol = key if key.startswith('i-') else ICON_ALIASES.get(key, 'i-sparkles')
    # width/height attributes are a hard fallback: without them an <svg> with no
    # CSS defaults to 300x150, which is what makes buttons and icons look
    # enormous whenever the stylesheet is missing, stale or still loading.
    # CSS rules override these attributes, so explicit sizes still win.
    return format_html(
        '<svg class="ico-svg {}" width="18" height="18" viewBox="0 0 24 24" '
        'aria-hidden="true" focusable="false"><use href="#{}"></use></svg>', cls, symbol)


@register.filter
def amenity_icon(amenity):
    key = getattr(amenity, 'icon', '') or ''
    symbol = ICON_ALIASES.get((key or '').strip().lower(), 'i-sparkles')
    return symbol


@register.filter
def bdt(value):
    return m.money(value)


@register.filter
def short_money(value):
    return m.short_bdt(value)


@register.filter
def lakh(value):
    try:
        return f'{float(value) / 100000:.1f}'
    except (TypeError, ValueError):
        return ''


@register.simple_tag
def meters(value):
    try:
        return f'{float(value) * 1000:.0f}'
    except (TypeError, ValueError):
        return ''


@register.simple_tag
def date_label(value, fmt='%b %Y'):
    if not value:
        return '—'
    return value.strftime(fmt)


@register.filter
def pct_of(value, total):
    try:
        return round(float(value) / float(total) * 100, 1)
    except (TypeError, ValueError, ZeroDivisionError):
        return 0


@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (TypeError, ValueError, ZeroDivisionError):
        return 0


@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (TypeError, ValueError):
        return 0


@register.simple_tag(takes_context=True)
def query_toggle(context, key, value):
    """Build a querystring toggling one value inside a multi-select filter."""
    request = context['request']
    params = request.GET.copy()
    values = params.getlist(key)
    if value in values:
        values = [v for v in values if v != value]
    else:
        values.append(value)
    params.setlist(key, values)
    params.pop('page', None)
    return params.urlencode()


@register.simple_tag(takes_context=True)
def query_set(context, **kwargs):
    request = context['request']
    params = request.GET.copy()
    for key, value in kwargs.items():
        if value in (None, ''):
            params.pop(key, None)
        else:
            params[key] = value
    params.pop('page', None)
    return params.urlencode()


@register.simple_tag(takes_context=True)
def is_filtered(context, key, value):
    return value in context['request'].GET.getlist(key)


@register.simple_tag(takes_context=True)
def has_filters(context):
    ignore = {'page', 'sort'}
    return any(k for k in context['request'].GET if k not in ignore)


@register.filter
def get_item(dictionary, key):
    if not dictionary:
        return None
    return dictionary.get(key)


@register.filter
def yt_id(url):
    if not url:
        return ''
    if 'v=' in url:
        return url.split('v=')[-1].split('&')[0]
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    return ''


@register.filter
def video_src(url):
    return m.video_embed(url) or ''


@register.filter
def first_item(seq):
    try:
        return next(iter(seq))
    except (StopIteration, TypeError):
        return None


@register.filter
def stars(value):
    try:
        n = int(value)
    except (TypeError, ValueError):
        n = 5
    return range(n)


@register.filter
def stage_color(stage):
    return {'ongoing': '#2f7d5a', 'upcoming': '#b3742f',
            'handover': '#3b6ea5', 'ready': '#1f8a70'}.get(stage, '#0c1f26')


# ---------------------------------------------------------------------------
# language helpers
# ---------------------------------------------------------------------------
@register.simple_tag(takes_context=True)
def t(context, key, default=''):
    """Translate a UI label. Falls back to ``default`` then the key itself.

    Usage:  {% t 'nav.projects' 'Projects' %}
    """
    if context.get('lang') != 'bn':
        return default or key
    return BN.get(key, default or key)


@register.simple_tag(takes_context=True)
def bn_num(context, value):
    """Render digits in Bengali numerals when the UI is in Bengali."""
    if context.get('lang') != 'bn':
        return value
    return str(value).translate(BN_DIGITS)


@register.filter
def bn_digits(value):
    return str(value).translate(BN_DIGITS)
