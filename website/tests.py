"""Smoke + behaviour tests for the redesigned STI Builders website.

Run with:  python manage.py test website
"""
import datetime as dt

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

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
        res = self.client.get(reverse('website:home'))
        html = res.content.decode()
        self.assertNotIn('&lt;svg', html)
        self.assertNotIn('&lt;use', html)
        self.assertIn('<use href="#i-', html)
        # every reference must point at a symbol that exists in the sprite
        import re
        defined = set(re.findall(r'<symbol id="([^"]+)"', html))
        referenced = set(re.findall(r'<use href="#([^"]+)"', html))
        self.assertTrue(referenced <= defined, referenced - defined)

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

    def test_footer_uses_dark_image_band(self):
        res = self.client.get(reverse('website:home'))
        self.assertContains(res, 'site-footer has-image')
        self.assertContains(res, 'footer-tower.jpg')

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
