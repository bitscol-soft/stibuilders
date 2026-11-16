"""Middleware for hosting the app inside the Arena preview iframe.

Two problems this solves, both learned the hard way:

1. Django's ``XFrameOptionsMiddleware`` writes ``settings.X_FRAME_OPTIONS``
   verbatim. There is no "omit the header" sentinel — the oft-cited
   ``'ALLOWALL'`` is not a real directive — so we keep a valid ``SAMEORIGIN``
   and delete the header on public pages here instead.

2. A ``frame-ancestors`` list of ``'self' https:`` still refuses an **http**
   parent origin, which is exactly what a local or non-TLS preview host is.
   The browser reports this as ``ERR_BLOCKED_BY_RESPONSE`` and the preview
   shows a blank frame, so the relaxed policy must not use a scheme allowlist.
"""
from django.conf import settings


class PreviewFrameMiddleware:
    #: Admin and CMS keep clickjacking protection regardless of preview mode.
    PROTECTED_PREFIXES = ('/admin/', '/cms/', '/property/')

    #: Deliberately scheme-agnostic: covers https previews, http sandboxes and
    #: dashboards embedded from a different port on 127.0.0.1.
    PREVIEW_CSP = "frame-ancestors *"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if getattr(settings, 'FRAME_GUARD_ENABLED', False):
            return response
        if request.path.startswith(self.PROTECTED_PREFIXES):
            return response

        if 'X-Frame-Options' in response.headers:
            del response.headers['X-Frame-Options']
        response.headers['Content-Security-Policy'] = self.PREVIEW_CSP
        return response
