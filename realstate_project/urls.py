"""realstate_project URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView

from website.sitemaps import (LocationSitemap, NewsSitemap, ProjectSitemap, ServiceSitemap,
                              StaticSitemap)

sitemaps = {
    'static': StaticSitemap,
    'projects': ProjectSitemap,
    'locations': LocationSitemap,
    'services': ServiceSitemap,
    'news': NewsSitemap,
}

admin.site.site_header = "STI Builders — Admin"
admin.site.site_title = "STI Builders Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    # legacy dashboard / CMS routes kept available under /cms/
    path('cms/', include('realstateapp.urls')),
    path('property/', include('property.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # legacy public URLs -> new information architecture (keeps old links alive)
    path('dashboard-login/', RedirectView.as_view(url='/cms/dashboard-login/', permanent=True)),
    path('dashboard-page/', RedirectView.as_view(url='/cms/dashboard-page/', permanent=True)),
    path('browse-all-property/', RedirectView.as_view(url='/projects/', permanent=True)),
    path('property-search/', RedirectView.as_view(url='/projects/', permanent=True)),
    path('search-result/', RedirectView.as_view(url='/projects/', permanent=True)),
    path('about-us/', RedirectView.as_view(url='/about/', permanent=True)),
    path('contact-us/', RedirectView.as_view(url='/contact/', permanent=True)),
    path('client-testimonial/', RedirectView.as_view(url='/about/#testimonials', permanent=True)),
    path('privacy-policy/', RedirectView.as_view(url='/faq/', permanent=True)),
    path('terms-conditions/', RedirectView.as_view(url='/faq/', permanent=True)),
    path('frequently-question/', RedirectView.as_view(url='/faq/', permanent=True)),
    path('slider-list/', RedirectView.as_view(url='/cms/slider-list/', permanent=True)),
]

# Uploaded media is served by Django for this deployment. In production put a
# CDN / object storage in front of MEDIA_URL instead of hitting this view.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
