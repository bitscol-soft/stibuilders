"""Language + theme state for every template."""

LANG_COOKIE = 'sti_lang'
THEME_COOKIE = 'sti_theme'
SUPPORTED_LANGS = ('en', 'bn')


def prefs(request):
    lang = request.COOKIES.get(LANG_COOKIE, 'en')
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    theme = request.COOKIES.get(THEME_COOKIE, 'light')
    if theme not in ('light', 'dark'):
        theme = 'light'
    return {
        'lang': lang,
        'lang_is_bn': lang == 'bn',
        'other_lang': 'en' if lang == 'bn' else 'bn',
        'theme': theme,
        'is_dark': theme == 'dark',
    }
