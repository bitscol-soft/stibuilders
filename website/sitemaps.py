from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Location, NewsPost, Project, Service


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Project.objects.live()

    def lastmod(self, obj):
        return obj.updated_at


class LocationSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Location.objects.filter(status=True)


class ServiceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Service.objects.filter(status=True)


class NewsSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return NewsPost.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_at


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    names = ['home', 'project_list', 'suburb_list', 'about', 'services', 'land_sharing',
             'investors', 'news', 'gallery', 'contact', 'faq', 'booking']

    def items(self):
        return self.names

    def location(self, item):
        return reverse(f'website:{item}')
