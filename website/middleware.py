"""Middleware for hosting the app inside the Arena preview iframe.

Django's ``XFrameOptionsMiddleware`` writes ``settings.X_FRAME_OPTIONS`` to the
response verbatim. There is no "omit the header" sentinel: the commonly seen
``'ALLOWALL'`` is not a valid value and browsers handle it inconsistently, so we
never emit it.

Instead ``X_FRAME_OPTIONS`` stays at a valid ``SAMEORIGIN`` and this middleware,
placed after Django's, removes the header for public pages while leaving the
admin protected. When real frame guarding is wanted for a public deployment,
set ``DJANGO_FRAME_GUARD=1`` and this middleware stands down.
"""
from django.conf import settings


class PreviewFrameMiddleware:
    #: Admin and CMS keep clickjacking protection regardless of preview mode.
    PROTECTED_PREFIXES = ('/admin/', '/cms/', '/property/')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if getattr(settings, 'FRAME_GUARD_ENABLED', False):
            return response
        if request.path.startswith(self.PROTECTED_PREFIXES):
            return response

        # Let a cross-origin preview host embed the page.
        if 'X-Frame-Options' in response.headers:
            del response.headers['X-Frame-Options']
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https:"
        return response
