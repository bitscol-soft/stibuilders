"""Seed the redesigned STI Builders website with realistic demo content.

Usage:  python manage.py seed_website
        python manage.py seed_website --reset
"""
import datetime as dt
import shutil
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import (Amenity, Apartment, Booking, Enquiry, Faq, Feature, GalleryImage,
                            Landmark, Location, Milestone, NewsPost, PaymentStage, Project,
                            ProjectFloorPlan, ProjectImage, Service, SiteSetting, TeamMember,
                            Testimonial)

IMG = Path(settings.BASE_DIR) / 'website' / 'static' / 'website' / 'img'
PLANS = IMG / 'plans'


def attach(field, relative_path):
    """Copy a bundled image into MEDIA_ROOT and assign it to an ImageField."""
    src = IMG / relative_path
    if not src.exists():
        src = IMG / 'projects' / relative_path
    if not src.exists():
        src = IMG / 'gallery' / relative_path
    if not src.exists():
        return
    from django.core.files.storage import default_storage
    rel = f'website/seed/{relative_path}'
    if not default_storage.exists(rel):
        with open(src, 'rb') as fh:
            default_storage.save(rel, File(fh))
    field.name = rel


def load_plan(field, name):
    src = PLANS / name
    if not src.exists():
        return
    from django.core.files.storage import default_storage
    rel = f'website/seed/plans/{name}'
    if not default_storage.exists(rel):
        with open(src, 'rb') as fh:
            default_storage.save(rel, File(fh))
    field.name = rel


class Command(BaseCommand):
    help = 'Populate the website app with demo projects, suburbs, units and editorial content.'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='Delete existing website data first')

    def handle(self, *args, **options):
        if options['reset']:
            for model in (Booking, Enquiry, Apartment, Milestone, PaymentStage, ProjectFloorPlan,
                          ProjectImage, Project, GalleryImage, NewsPost, Testimonial, TeamMember,
                          Service, Faq, Landmark, Amenity, Feature, Location, SiteSetting):
                model.objects.all().delete()
            self.stdout.write('Cleared existing website data.')

        today = timezone.now().date()
        self.site_setting()
        amenities = self.amenities()
        features = self.features()
        locations = self.locations(amenities)
        self.services()
        self.team()
        self.faqs()
        self.projects(locations, amenities, features, today)
        self.testimonials()
        self.news()
        self.gallery()
        self.stdout.write(self.style.SUCCESS('✔ Website demo content ready.'))

    # ------------------------------------------------------------------
    def site_setting(self):
        s = SiteSetting.objects.first() or SiteSetting()
        s.company_name = 'STI Builders Limited'
        s.tagline = 'Building trusted addresses across Dhaka'
        s.phone = '01923505050'
        s.phone_2 = '01322301173'
        s.hotline = '09612 119 911'
        s.email = 'info@stibuilderslimited.com'
        s.sales_email = 'sales@stibuilderslimited.com'
        s.address = ('House 41 (Flat A2, Level 02), Sonargaon Janapath Road, '
                     'Sector 12, Uttara Model Town, Dhaka 1230')
        s.office_hours = 'Saturday – Thursday · 10:00 AM – 7:00 PM'
        s.whatsapp = '8801923505050'
        s.facebook = 'https://facebook.com/stibuilderslimited'
        s.instagram = 'https://instagram.com/stibuilderslimited'
        s.youtube = 'https://youtube.com/@stibuilderslimited'
        s.linkedin = 'https://linkedin.com/company/stibuilderslimited'
        s.about_short = ('Building considered addresses across Dhaka since 2012 — apartments, '
                         'commercial floors and land-sharing developments delivered with structural '
                         'integrity and quiet elegance.')
        s.years_experience = 14
        s.projects_delivered = 26
        s.happy_families = 1840
        s.sqft_delivered = 2400000
        s.save()
        self.site = s

    def amenities(self):
        data = [
            ('Swimming Pool', 'pool', 'Rooftop, 25 m lap'),
            ('Gymnasium', 'gym', 'Air-conditioned, 3rd floor'),
            ('Covered Parking', 'parking', 'Sub + ground level'),
            ('High-speed Lifts', 'lift', '2 × 8 passenger'),
            ('Generator & IPS', 'generator', '100% common area back-up'),
            ('24/7 Security', 'security', 'Trained guards, visitor log'),
            ('CCTV Coverage', 'cctv', 'Lobby, lifts, parking'),
            ('Roof Garden', 'roof', 'Landscaped with seating'),
            ('Community Lounge', 'lounge', 'Residents only'),
            ('Kids Play Area', 'play', 'Rubberised surface'),
            ('Prayer Space', 'mosque', 'Ground floor'),
            ('Landscaped Garden', 'garden', 'Native planting'),
            ('Water Treatment', 'water', 'Softener + filtration'),
            ('Fire Fighting', 'fire', 'Hydrant, sprinkler, alarm'),
            ('Community Wi-Fi', 'wifi', 'Lobby & lounge'),
            ('Club House', 'club', 'Party & meeting room'),
            ('Power Sub-station', 'power', 'Dedicated DPDC connection'),
            ('Intercom', 'intercom', 'Unit to guard post'),
            ('Laundry Service', 'laundry', 'Optional, basement'),
            ('EV Charging', 'ev', '2 bays, basement'),
        ]
        out = []
        for i, (name, icon, note) in enumerate(data):
            obj, _ = Amenity.objects.get_or_create(name=name,
                                                   defaults={'icon': icon, 'note': note, 'order': i})
            obj.icon, obj.note, obj.order = icon, note, i
            obj.save()
            out.append(obj)
        return out

    def features(self):
        names = [
            'Imported ceramic tiles (living & dining)', 'Imported sanitary ware',
            'Concealed electrical wiring', 'Teak wood main door', 'Flush wooden doors',
            'Powder-coated aluminium windows', 'Granite kitchen counter',
            'Anti-termite treatment', 'CCTV-ready conduit', 'Split AC provision in bedrooms',
            'Walk-in closet (master)', 'Rainwater harvesting provision',
            'Basement car parking', 'Intercom facility', 'Solar-ready roof conduit',
        ]
        out = []
        for i, n in enumerate(names):
            obj, _ = Feature.objects.get_or_create(name=n, defaults={'order': i})
            out.append(obj)
        return out

    def locations(self, amenities):
        data = [
            dict(name='Uttara', zone='North Dhaka', lat='23.8759', lng='90.3795',
                 note='Metro corridor, wide sector roads and the strongest rental demand in north Dhaka.',
                 price=9200, growth=7.4, yld=5.1, demand=88, live=84, commute=42,
                 schools=34, hospitals=11, malls=6, green=18,
                 h1='Walking distance to Metro Rail stations 2 & 3',
                 h2='Hazrat Shahjalal International Airport — 18 minutes',
                 h3='Sector roads 40–100 ft wide, low waterlogging',
                 road='40–100 ft roads', image='proj-uttara.jpg',
                 landmarks=[('Uttara Metro Station 3', 'metro', 0.9, 4),
                            ('Hazrat Shahjalal Airport', 'airport', 7.4, 18),
                            ('International University of Business Agriculture', 'school', 2.1, 8),
                            ('Kuwait Bangladesh Friendship Government Hospital', 'hospital', 3.3, 11),
                            ('Rajlaxmi Complex', 'mall', 2.6, 9),
                            ('Uttara Sector 4 Lake Park', 'park', 1.4, 5)]),
            dict(name='Bashundhara R/A', zone='North-East Dhaka', lat='23.8223', lng='90.4267',
                 note='Planned residential blocks, lakes and the new diplomatic zone next door.',
                 price=8600, growth=8.9, yld=4.7, demand=83, live=88, commute=58,
                 schools=41, hospitals=9, malls=7, green=31,
                 h1='Lake-facing plots with walking trails',
                 h2='Adjacent to the new diplomatic enclave',
                 h3='School cluster within 3 km',
                 road='60–120 ft roads', image='proj-bashundhara.jpg',
                 landmarks=[('International School Dhaka', 'school', 1.8, 6),
                            ('Evercare Hospital', 'hospital', 2.9, 9),
                            ('Jamuna Future Park', 'mall', 3.6, 12),
                            ('Bashundhara lake walk', 'park', 0.4, 2),
                            ('Kuril Flyover (airport road)', 'office', 2.2, 7)]),
            dict(name='Gulshan', zone='Central Dhaka', lat='23.7806', lng='90.4158',
                 note='The diplomatic quarter — boutique buildings, embassies and premium rents.',
                 price=21500, growth=5.2, yld=4.2, demand=76, live=91, commute=35,
                 schools=18, hospitals=8, malls=9, green=22,
                 h1='Embassies, corporates and top restaurants within 2 km',
                 h2='Highest rental yield per sq ft in the city',
                 h3='Wide avenue frontage, low density',
                 road='60–80 ft roads', image='proj-gulshan.jpg',
                 landmarks=[('Gulshan 2 Circle', 'office', 0.8, 3),
                            ('Banani Metro Station', 'metro', 1.9, 7),
                            ('Scholastica (Gulshan)', 'school', 1.1, 4),
                            ('United Hospital', 'hospital', 2.4, 8),
                            ('Gulshan Lake Park', 'park', 0.9, 4)]),
            dict(name='Dhanmondi', zone='Central-West Dhaka', lat='23.7461,', lng='90.3763',
                 note='Established, leafy and walkable — established families and stable resale.',
                 price=17800, growth=4.6, yld=4.0, demand=71, live=86, commute=28,
                 schools=29, hospitals=12, malls=5, green=24,
                 h1='Dhanmondi Lake and Rabindra Sarobar nearby',
                 h2='Strong resale market, stable prices',
                 h3='Hospitals and schools within walking distance',
                 road='40–60 ft roads', image='proj-dhanmondi.jpg',
                 landmarks=[('Dhanmondi Lake', 'park', 0.7, 3),
                            ('Square Hospital', 'hospital', 1.3, 5),
                            ('Dhaka College', 'school', 1.6, 6),
                            ('Metro Rail (Farmgate)', 'metro', 2.8, 10),
                            ('Rapa Plaza', 'mall', 0.9, 4)]),
            dict(name='Purbachal', zone='East Dhaka', lat='23.8325', lng='90.5210',
                 note='Planned satellite city — wide roads, plotted development and long-run upside.',
                 price=5600, growth=11.8, yld=3.4, demand=69, live=74, commute=62,
                 schools=12, hospitals=4, malls=2, green=44,
                 h1='Planned 300 ft arterial roads',
                 h2='Lowest per-sq-ft entry in our portfolio',
                 h3='Government-backed master plan',
                 road='100–300 ft roads', image='proj-purbachal.jpg',
                 landmarks=[('Purbachal Expressway', 'office', 1.2, 4),
                            ('Kuril Bishwa Road', 'metro', 12.4, 32),
                            ('Purbachal Lake', 'park', 0.6, 3),
                            ('International Convention City', 'mall', 9.8, 26)]),
            dict(name='Banani', zone='Central Dhaka', lat='23.7936,', lng='90.4043',
                 note='Commercial heart with the metro at the door — ideal for office floors.',
                 price=19800, growth=6.1, yld=5.4, demand=74, live=82, commute=31,
                 schools=14, hospitals=6, malls=8, green=15,
                 h1='Banani Metro Station within 500 m',
                 h2='Corporate tenant pool on the doorstep',
                 h3='Highest commercial rental demand in north Dhaka',
                 road='60–80 ft roads', image='proj-banani.jpg',
                 landmarks=[('Banani Metro Station', 'metro', 0.5, 2),
                            ('Gulshan 2 Circle', 'office', 1.4, 5),
                            ('Banani Club', 'park', 0.8, 3),
                            ('CIty Bank Tower, Gulshan', 'office', 1.1, 4)]),
        ]
        out = {}
        for i, d in enumerate(data):
            loc, _ = Location.objects.get_or_create(name=d['name'])
            loc.city = 'Dhaka'
            loc.zone = d['zone']
            loc.short_note = d['note']
            loc.description = (f"<p>{d['note']} Our team has been active here since "
                               f"{2016 + i % 4}, and we maintain a live price sheet from signed "
                               f"transactions rather than advertised rates.</p>")
            loc.latitude = float(d['lat'].strip(','))
            loc.longitude = float(d['lng'])
            loc.avg_price_per_sqft = d['price']
            loc.price_growth_yoy = d['growth']
            loc.rental_yield = d['yld']
            loc.demand_index = d['demand']
            loc.livability_score = d['live']
            loc.commute_minutes = d['commute']
            loc.schools_count = d['schools']
            loc.hospitals_count = d['hospitals']
            loc.malls_count = d['malls']
            loc.green_space_pct = d['green']
            loc.highlight_1 = d['h1']
            loc.highlight_2 = d['h2']
            loc.highlight_3 = d['h3']
            loc.road_access = d['road']
            loc.order = i
            loc.status = True
            attach(loc.cover_image, d['image'])
            loc.save()
            out[d['name']] = loc

            for j, (name, cat, dist, mins) in enumerate(d['landmarks']):
                Landmark.objects.update_or_create(
                    location=loc, name=name,
                    defaults={'category': cat, 'distance_km': dist,
                              'drive_minutes': mins, 'order': j, 'status': True})
        return out

    def projects(self, locations, amenities, features, today):
        amen_by_icon = {a.icon: a for a in amenities}
        data = [
            dict(
                name='STI Royal Tower', slug='sti-royal-tower', loc='Uttara',
                stage='ongoing', category='residential', ownership='freehold',
                tagline='Fourteen storeys on Sonargaon Janapath — our flagship address in Uttara.',
                cover='proj-gulshan.jpg', night='hero-tower.jpg',
                gallery=['proj-gulshan.jpg', 'interior-living.jpg', 'interior-kitchen.jpg',
                         'proj-royal-1.jpg', 'int-2.jpg', 'proj-royal-2.jpg'],
                floors=14, basement=2, units=42, upf=3, lifts=2, stairs=2, parking=42,
                land=8.5, facing='South-East', road='60 ft', plot='12', block='C',
                architect='Residence Studio, Dhaka', structural='STI Engineering',
                rajuk='RAJUK/24/STI/0142', handover=dt.date(2027, 6, 30), launch=dt.date(2024, 3, 1),
                pct=58, price=15800000, ppsf=8540, size_from=1450, size_to=2300, beds_from=3, beds_to=4,
                booking=1500000, featured=True, order=1,
                amenities=['pool', 'gym', 'parking', 'lift', 'generator', 'security', 'cctv', 'roof',
                           'lounge', 'fire', 'water', 'intercom'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=52, dev=48,
                map=(23.8749, 90.3792),
                desc=('<p>Royal Tower is a fourteen-storey residential address on Sonargaon Janapath, '
                      'a three-minute walk from Uttara’s metro corridor. Three apartments per floor '
                      'are planned around a south-east orientation so that every living room gets '
                      'morning light and every bedroom gets cross ventilation.</p>'
                      '<p>The structure is an RCC frame designed to BNBC 2020, with two basement '
                      'levels of parking, a rooftop pool deck and a residents-only lounge at the '
                      'third-floor setback.</p>'),
                concept=('We shaped the plan around the sun, not the site boundary. Every unit has '
                         'at least two faces, so no family lives in a corridor-facing room.'),
                milestones=[('Land acquisition & title clearance', -540, 100, True),
                            ('RAJUK approval & piling', -420, 100, True),
                            ('Basement & foundation', -300, 100, True),
                            ('Structure up to 8th floor', -90, 100, True),
                            ('Structure up to roof level', 90, 45, False),
                            ('Brickwork & plastering', 180, 15, False),
                            ('Finishing, lifts & utilities', 300, 5, False),
                            ('Snag, handover & mutation support', 420, 0, False)],
                units_data=[('A', '3bed', 'Type A — Corner', 1850, 3, 3, 2, 2, 'South-East', 15800000, 'available'),
                            ('B', '4bed', 'Type B — Lake view', 2300, 4, 4, 3, 2, 'South', 19650000, 'available'),
                            ('C', '3bed', 'Type C — Garden', 1620, 3, 3, 2, 1, 'North-East', 13850000, 'booked'),
                            ('D', '4bed', 'Type D — Duplex', 2450, 4, 4, 3, 2, 'South-West', 22100000, 'available'),
                            ('E', '3bed', 'Type E', 1450, 3, 3, 1, 1, 'East', 12250000, 'sold')],
            ),
            dict(
                name='STI Lake Drive Paradise', slug='sti-lake-drive-paradise', loc='Bashundhara R/A',
                stage='ongoing', category='residential', ownership='freehold',
                tagline='Eleven storeys facing the lake — cross-ventilated homes with a private jetty walk.',
                cover='proj-bashundhara.jpg', night='proj-bashundhara.jpg',
                gallery=['proj-bashundhara.jpg', 'proj-bashundhara-2.jpg', 'int-1.jpg',
                         'int-3.jpg', 'proj-lake-1.jpg'],
                floors=11, basement=1, units=33, upf=3, lifts=2, stairs=2, parking=36,
                land=7.2, facing='West (lake)', road='80 ft', plot='44', block='D',
                architect='Delta Design Collective', structural='STI Engineering',
                rajuk='RAJUK/24/STI/0151', handover=dt.date(2026, 12, 31), launch=dt.date(2023, 11, 1),
                pct=74, price=16900000, ppsf=9100, size_from=1650, size_to=2480, beds_from=3, beds_to=4,
                booking=1800000, featured=True, order=2,
                amenities=['pool', 'gym', 'parking', 'lift', 'generator', 'security', 'cctv',
                           'garden', 'play', 'club', 'fire', 'water'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ', 'https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=50, dev=50,
                map=(23.8226, 90.4271),
                desc=('<p>A lake-facing tower planned so that the western face is entirely open. '
                      'Three apartments per floor, each with a deep balcony that reads the water. '
                      'The building sits inside a planned block with 80 ft road frontage, giving '
                      'the fire tender and ambulance a straight approach.</p>')
                ,
                concept=('The lake is the client. Everything else — the cores, the parking, the '
                         'plant — is pushed to the rear so the living rooms can breathe.'),
                milestones=[('Land acquisition & feasibility', -620, 100, True),
                            ('RAJUK approval', -480, 100, True),
                            ('Piling & basement', -320, 100, True),
                            ('Structure up to 11th floor', -30, 100, True),
                            ('Brickwork & internal plaster', 60, 60, False),
                            ('Lifts, generator & utilities', 180, 25, False),
                            ('Handover', 300, 0, False)],
                units_data=[('A', '3bed', 'Type A — Lake view', 1650, 3, 3, 2, 1, 'West', 15200000, 'available'),
                            ('B', '4bed', 'Type B — Lake corner', 2480, 4, 4, 3, 2, 'West', 22800000, 'available'),
                            ('C', '3bed', 'Type C — Garden', 1780, 3, 3, 2, 2, 'East', 16100000, 'hold')],
            ),
            dict(
                name='STI Orchid Residences', slug='sti-orchid-residences', loc='Uttara',
                stage='upcoming', category='residential', ownership='landshare',
                tagline='Launching winter 2026 — a quiet nine-storey street address off Sector 15.',
                cover='proj-orchid-1.jpg', night='proj-gulshan.jpg',
                gallery=['proj-orchid-1.jpg', 'proj-gulshan.jpg', 'int-2.jpg'],
                floors=9, basement=1, units=27, upf=3, lifts=2, stairs=2, parking=28,
                land=5.8, facing='South', road='40 ft', plot='7', block='A',
                architect='Residence Studio, Dhaka', structural='STI Engineering',
                rajuk='Applied', handover=dt.date(2028, 6, 30), launch=dt.date(2026, 1, 15),
                pct=6, price=11200000, ppsf=7600, size_from=1180, size_to=1780, beds_from=2, beds_to=3,
                booking=1000000, featured=True, order=3,
                amenities=['parking', 'lift', 'generator', 'security', 'roof', 'fire', 'water', 'intercom'],
                videos=[],
                land_owner=55, dev=45,
                map=(23.8681, 90.3866),
                desc=('<p>Orchid is a smaller, quieter building: three apartments per floor, a '
                      'single basement of parking and a roof garden shared by twenty-seven families. '
                      'It is aimed at buyers who want Uttara’s connectivity without a tower crowd.</p>'),
                concept=('Small enough to know your neighbours, wide enough for a proper living room.'),
                milestones=[('Land sharing deed signed', -120, 100, True),
                            ('Drawing & RAJUK submission', 30, 40, False),
                            ('Piling & foundation', 150, 0, False),
                            ('Structure & finishing', 480, 0, False)],
                units_data=[('A', '2bed', 'Type A', 1180, 2, 2, 1, 1, 'South', 11200000, 'available'),
                            ('B', '3bed', 'Type B', 1560, 3, 3, 2, 1, 'South-East', 13400000, 'available'),
                            ('C', '3bed', 'Type C — Corner', 1780, 3, 3, 2, 2, 'East', 14750000, 'available')],
            ),
            dict(
                name='STI Textile Palace', slug='sti-textile-palace', loc='Uttara',
                stage='handover', category='residential', ownership='freehold',
                tagline='Delivered in 2022 — twelve storeys, 36 families, zero pending snags.',
                cover='proj-royal-2.jpg', night='proj-dhanmondi.jpg',
                gallery=['proj-royal-2.jpg', 'proj-dhanmondi-2.jpg', 'int-3.jpg', 'proj-royal-1.jpg'],
                floors=12, basement=1, units=36, upf=3, lifts=2, stairs=2, parking=38,
                land=8.0, facing='South-West', road='60 ft', plot='19', block='B',
                architect='Vertex Architects', structural='STI Engineering',
                rajuk='RAJUK/19/STI/0087', handover=dt.date(2022, 9, 30), launch=dt.date(2019, 4, 1),
                pct=100, price=None, ppsf=None, size_from=1350, size_to=1980, beds_from=3, beds_to=3,
                booking=None, featured=False, order=4,
                amenities=['parking', 'lift', 'generator', 'security', 'cctv', 'roof', 'fire', 'intercom'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=None, dev=None,
                map=(23.8702, 90.3921),
                desc=('<p>Handed over on schedule in September 2022, Textile Palace is now fully '
                      'occupied. It is the clearest evidence of what we promise: the finishing in '
                      'the building matches the finishing in the brochure, four years on.</p>'),
                concept=('A building proves itself after handover. This one has been proving it since 2022.'),
                milestones=[('Foundation', -1100, 100, True), ('Structure', -800, 100, True),
                            ('Finishing', -420, 100, True), ('Handover', -300, 100, True)],
                units_data=[('A', '3bed', 'Type A', 1350, 3, 3, 1, 1, 'South-West', None, 'sold'),
                            ('B', '3bed', 'Type B', 1980, 3, 3, 2, 2, 'South', None, 'sold')],
            ),
            dict(
                name='STI Dhanmondi Court', slug='sti-dhanmondi-court', loc='Dhanmondi',
                stage='ready', category='residential', ownership='freehold',
                tagline='Ready to move — eight storeys, only three apartments still unsold.',
                cover='proj-dhanmondi.jpg', night='proj-dhanmondi-2.jpg',
                gallery=['proj-dhanmondi.jpg', 'proj-dhanmondi-2.jpg', 'interior-living.jpg',
                         'interior-bedroom.jpg'],
                floors=8, basement=0, units=16, upf=2, lifts=1, stairs=1, parking=18,
                land=4.2, facing='East', road='40 ft', plot='31', block='—',
                architect='Studio Dhaka', structural='STI Engineering',
                rajuk='RAJUK/21/STI/0119', handover=dt.date(2025, 12, 15), launch=dt.date(2022, 7, 1),
                pct=100, price=24500000, ppsf=12400, size_from=1920, size_to=2150, beds_from=3, beds_to=4,
                booking=2000000, featured=True, order=5,
                amenities=['parking', 'lift', 'generator', 'security', 'cctv', 'gym', 'roof',
                           'lounge', 'fire', 'water', 'intercom', 'laundry'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=48, dev=52,
                map=(23.7465, 90.3765),
                desc=('<p>An eight-storey boutique building on a quiet Dhanmondi lane, completed and '
                      'handed over in December 2025. Two apartments per floor, both corner, both with '
                      'a 12 ft deep balcony. Three units remain unsold and can be visited furnished.</p>'),
                concept=('Two families per floor. That is the whole idea.'),
                milestones=[('Foundation', -900, 100, True), ('Structure', -600, 100, True),
                            ('Finishing', -240, 100, True), ('Handover', -11, 100, True)],
                units_data=[('A', '3bed', 'Type A — Corner', 1920, 3, 3, 2, 1, 'East', 24500000, 'available'),
                            ('B', '4bed', 'Type B — Corner', 2150, 4, 4, 2, 2, 'North-East', 26800000, 'available'),
                            ('C', '3bed', 'Type C', 1980, 3, 3, 2, 1, 'West', None, 'sold')],
            ),
            dict(
                name='STI Purbachal Green Plots', slug='sti-purbachal-green-plots', loc='Purbachal',
                stage='upcoming', category='land', ownership='landshare',
                tagline='Ready plots on 100–300 ft roads with a planned lake park and mosque.',
                cover='proj-purbachal.jpg', night='land-1.jpg',
                gallery=['proj-purbachal.jpg', 'land-1.jpg', 'land-2.jpg', 'proj-purbachal.jpg'],
                floors=0, basement=0, units=48, upf=0, lifts=0, stairs=0, parking=0,
                land=105.0, land_unit='katha', facing='Various', road='100–300 ft', plot='—', block='—',
                architect='Purbachal master plan', structural='—',
                rajuk='RAJUK Purbachal allotment', handover=dt.date(2027, 3, 31), launch=dt.date(2025, 6, 1),
                pct=22, price=7200000, ppsf=2100, size_from=3, size_to=10, beds_from=None, beds_to=None,
                booking=700000, featured=False, order=6,
                amenities=['parking', 'security', 'mosque', 'garden', 'play', 'water', 'power'],
                videos=[],
                land_owner=52, dev=48,
                map=(23.8327, 90.5208),
                desc=('<p>Forty-eight residential plots inside the Purbachal planned area, sized '
                      'between three and ten katha, all with direct access to a 100 ft or wider road. '
                      'Development work — roads, drainage, water and electricity — is funded by the '
                      'land-sharing arrangement and delivered before registration.</p>'),
                concept=('Buy the road frontage, not just the plot. Every plot here opens onto a '
                         '100 ft or wider carriageway.'),
                milestones=[('Land pooling & deed', -300, 100, True),
                            ('RAJUK plan approval', 90, 45, False),
                            ('Roads, drainage & utilities', 300, 0, False),
                            ('Registration & handover', 480, 0, False)],
                units_data=[('P-01', 'plot', '3 katha plot', 3, None, None, None, None, 'South', 7200000, 'available'),
                            ('P-02', 'plot', '5 katha plot', 5, None, None, None, None, 'East', 11200000, 'available'),
                            ('P-03', 'plot', '10 katha corner plot', 10, None, None, None, None, 'North', 22500000, 'hold')],
            ),
            dict(
                name='STI Banani Business Square', slug='sti-banani-business-square', loc='Banani',
                stage='ongoing', category='commercial', ownership='joint',
                tagline='Nine floors of Grade-A office space, 500 m from Banani metro.',
                cover='proj-banani.jpg', night='proj-banani.jpg',
                gallery=['proj-banani.jpg', 'interior-kitchen.jpg', 'proj-gulshan.jpg'],
                floors=9, basement=2, units=18, upf=2, lifts=2, stairs=2, parking=34,
                land=6.4, facing='West', road='80 ft', plot='5', block='—',
                architect='Form & Function', structural='STI Engineering',
                rajuk='RAJUK/25/STI/0163', handover=dt.date(2027, 3, 31), launch=dt.date(2025, 2, 1),
                pct=41, price=38000000, ppsf=13800, size_from=2400, size_to=3200, beds_from=None, beds_to=None,
                booking=3000000, featured=False, order=7,
                amenities=['parking', 'lift', 'generator', 'security', 'cctv', 'fire', 'wifi',
                           'power', 'ev', 'intercom'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=45, dev=55,
                map=(23.7939, 90.4046),
                desc=('<p>A nine-storey commercial building designed for a single corporate tenant '
                      'per floor. Each floor plate is 2,400–3,200 sq ft, column-free, with its own '
                      'washroom core and dedicated lift lobby. Two basement levels provide 34 car '
                      'spaces with EV charging bays.</p>'),
                concept=('Office floors that a company can grow into — and shrink within, without '
                         'moving buildings.'),
                milestones=[('Feasibility & joint-venture deed', -420, 100, True),
                            ('RAJUK approval', -240, 100, True),
                            ('Piling & basement', -90, 100, True),
                            ('Structure up to 5th floor', 60, 55, False),
                            ('Structure to roof & glazing', 210, 0, False),
                            ('Fit-out & handover', 330, 0, False)],
                units_data=[('201', 'office', '2nd floor — full plate', 2400, None, None, None, 2, 'West', 38000000, 'available'),
                            ('401', 'office', '4th floor — full plate', 2800, None, None, None, 2, 'West', 42500000, 'available'),
                            ('601', 'office', '6th floor — half plate', 1500, None, None, None, 1, 'West', 24500000, 'booked')],
            ),
            dict(
                name='STI Gulshan Prive', slug='sti-gulshan-prive', loc='Gulshan',
                stage='ready', category='residential', ownership='freehold',
                tagline='Twelve residences, two per floor, in the diplomatic quarter.',
                cover='proj-gulshan.jpg', night='hero-tower.jpg',
                gallery=['proj-gulshan.jpg', 'interior-living.jpg', 'interior-bedroom.jpg',
                         'interior-kitchen.jpg', 'hero-tower.jpg'],
                floors=8, basement=2, units=12, upf=2, lifts=2, stairs=2, parking=24,
                land=4.8, facing='North-West', road='60 ft', plot='9', block='—',
                architect='Atelier Dhaka', structural='STI Engineering',
                rajuk='RAJUK/22/STI/0131', handover=dt.date(2026, 2, 28), launch=dt.date(2023, 1, 1),
                pct=100, price=52000000, ppsf=19800, size_from=2620, size_to=3100, beds_from=4, beds_to=5,
                booking=5000000, featured=True, order=8,
                amenities=['pool', 'gym', 'parking', 'lift', 'generator', 'security', 'cctv', 'roof',
                           'lounge', 'club', 'fire', 'water', 'intercom', 'laundry', 'ev'],
                videos=['https://www.youtube.com/embed/aqz-KE-bpKQ'],
                land_owner=48, dev=52,
                map=(23.7809, 90.4161),
                desc=('<p>Twelve apartments across eight floors, two per level, each with a private '
                      'lift lobby. The building is finished and occupied, with one penthouse '
                      'available for viewing by appointment.</p>'),
                concept=('In Gulshan, privacy is the amenity. Two homes per floor gives that '
                         'without a gated compound.'),
                milestones=[('Land acquisition', -1200, 100, True), ('Structure', -700, 100, True),
                            ('Finishing & landscaping', -300, 100, True), ('Handover', -120, 100, True)],
                units_data=[('PH', '5bed', 'Penthouse — duplex', 3100, 5, 5, 4, 3, 'North-West', 52000000, 'available'),
                            ('A', '4bed', 'Type A', 2620, 4, 4, 3, 2, 'North-West', 44800000, 'sold')],
            ),
            dict(
                name='STI Uttara Central', slug='sti-uttara-central', loc='Uttara',
                stage='ongoing', category='mixed', ownership='joint',
                tagline='Retail on the ground, offices above, and twelve apartments on top.',
                cover='proj-uttara.jpg', night='proj-uttara.jpg',
                gallery=['proj-uttara.jpg', 'proj-royal-1.jpg', 'int-1.jpg'],
                floors=13, basement=2, units=24, upf=2, lifts=3, stairs=2, parking=40,
                land=9.1, facing='South', road='100 ft', plot='2', block='Sector 7',
                architect='Metro Design Studio', structural='STI Engineering',
                rajuk='RAJUK/25/STI/0177', handover=dt.date(2028, 3, 31), launch=dt.date(2025, 9, 1),
                pct=18, price=9600000, ppsf=8200, size_from=980, size_to=1950, beds_from=2, beds_to=3,
                booking=900000, featured=False, order=9,
                amenities=['parking', 'lift', 'generator', 'security', 'cctv', 'wifi', 'power',
                           'fire', 'roof', 'intercom'],
                videos=[],
                land_owner=46, dev=54,
                map=(23.8721, 90.3811),
                desc=('<p>A mixed-use address on a 100 ft road: retail at grade, two floors of '
                      'office, and twelve apartments above, served by a separate residential core '
                      'and lift bank so that residents never share a lobby with shoppers.</p>'),
                concept=('Commercial and residential cores kept completely separate — the single '
                         'detail that makes mixed-use work in Dhaka.'),
                milestones=[('Joint venture deed', -300, 100, True),
                            ('RAJUK approval', -120, 100, True),
                            ('Piling & basement', 90, 30, False),
                            ('Structure & handover', 600, 0, False)],
                units_data=[('A', '2bed', 'Type A', 980, 2, 2, 1, 1, 'South', 9600000, 'available'),
                            ('B', '3bed', 'Type B', 1520, 3, 3, 2, 1, 'South', 13400000, 'available'),
                            ('C', '3bed', 'Type C', 1950, 3, 3, 2, 2, 'South-East', 16800000, 'available')],
            ),
        ]

        for d in data:
            loc = locations[d['loc']]
            p = Project.objects.filter(slug=d['slug']).first() or Project(slug=d['slug'])
            p.name = d['name']
            p.tagline = d['tagline']
            p.code = 'STI-' + str(100 + d['order'])
            p.category = d['category']
            p.stage = d['stage']
            p.ownership = d['ownership']
            p.location = loc
            p.address = f"{loc.name}, Dhaka"
            p.short_description = d['tagline']
            p.description = d['desc']
            p.concept_note = d['concept']
            p.floors = d['floors']
            p.basement_levels = d['basement']
            p.total_units = d['units']
            p.units_per_floor = d['upf']
            p.lifts = d['lifts']
            p.staircases = d['stairs']
            p.parking_spaces = d['parking']
            p.land_area = d['land']
            p.land_area_unit = d.get('land_unit', 'katha')
            p.facing = d['facing']
            p.road_width = d['road']
            p.plot_no = d['plot']
            p.block_no = d['block']
            p.architect = d['architect']
            p.structural_consultant = d['structural']
            p.rajuk_number = d['rajuk']
            p.handover_date = d['handover']
            p.launch_date = d['launch']
            p.completion_pct = d['pct']
            p.price_from = d['price']
            p.price_per_sqft = d['ppsf']
            p.size_from = d['size_from']
            p.size_to = d['size_to']
            p.beds_from = d['beds_from']
            p.beds_to = d['beds_to']
            p.booking_amount = d['booking']
            p.map_latitude, p.map_longitude = d['map']
            p.social_hashtag = 'STIBuilders'
            p.facebook_url = 'https://facebook.com/stibuilderslimited'
            p.instagram_url = 'https://instagram.com/stibuilderslimited'
            p.youtube_url = 'https://youtube.com/@stibuilderslimited'
            p.featured = d['featured']
            p.order = d['order']
            p.published = True
            p.status = True
            if d['videos']:
                p.video_1_url = d['videos'][0]
                if len(d['videos']) > 1:
                    p.video_2_url = d['videos'][1]
            p.land_owner_share = d['land_owner']
            p.developer_share = d['dev']
            p.land_share_note = ('The owner’s share is handed over first at completion. Registration '
                                 'and mutation costs for the owner’s units are borne by STI Builders.')
            p.views = 120 + d['order'] * 37
            attach(p.cover_image, d['cover'])
            attach(p.night_image, d['night'])
            p.save()

            p.amenities.set([a for a in amenities if a.icon in d['amenities']])
            p.features.set(features[:10])

            # gallery
            p.images.all().delete()
            captions = ['Exterior view', 'Living & dining', 'Kitchen', 'Bedroom',
                        'Balcony', 'Construction progress', 'Roof terrace']
            for i, img in enumerate(d['gallery']):
                pi = ProjectImage(project=p, order=i,
                                  caption=captions[i % len(captions)],
                                  category='interior' if i in (1, 2, 3) else 'exterior')
                attach(pi.image, img)
                pi.save()
            for extra in ('interior-living.jpg', 'interior-kitchen.jpg', 'interior-bedroom.jpg'):
                pi = ProjectImage(project=p, order=len(d['gallery']) + 1,
                                  caption=extra.replace('.jpg', '').replace('-', ' ').title(),
                                  category='interior')
                attach(pi.image, extra)
                pi.save()

            # floor plans
            p.floor_plans.all().delete()
            if d['category'] != 'land':
                plan_a = ProjectFloorPlan(project=p, title='Unit Type A', kind='unit', order=0,
                                          area_sft=d['size_from'], beds=d['beds_from'],
                                          description='Corner unit with south-east living')
                load_plan(plan_a.image, 'floor-type-a.svg')
                plan_a.save()
                plan_b = ProjectFloorPlan(project=p, title='Unit Type B', kind='unit', order=1,
                                          area_sft=d['size_to'], beds=d['beds_to'],
                                          description='Larger layout with an extra balcony')
                load_plan(plan_b.image, 'floor-type-b.svg')
                plan_b.save()
            typical = ProjectFloorPlan(project=p, title='Typical floor plate', kind='floor', order=2,
                                       description='3 apartments per floor, 2 lifts + 2 stairs')
            load_plan(typical.image, 'floor-typical.svg')
            typical.save()
            site = ProjectFloorPlan(project=p, title='Site & master plan', kind='site', order=3,
                                    description='Land use, road frontage and open space study')
            load_plan(site.image, 'site-plan.svg')
            site.save()

            # milestones
            p.milestones.all().delete()
            for i, (title, day_offset, progress, done) in enumerate(d['milestones']):
                target = today + dt.timedelta(days=day_offset)
                Milestone.objects.create(
                    project=p, title=title, order=i, progress_pct=progress,
                    target_date=None if done else target,
                    completed_date=target if done else None,
                    is_done=done, status=True,
                    description='' if done else 'Tracked by the site engineer with monthly photographs.')
            p.milestones.filter(order=len(d['milestones']) - 1).update(is_done=d['stage'] in ('handover', 'ready'))

            # payment stages
            p.payment_stages.all().delete()
            stages = [
                ('Agreement signing', 10, 'On signing the buyer agreement', 'Booking money adjusted here'),
                ('Piling complete', 25, 'After foundation and piling', ''),
                ('5th floor slab', 30, 'On casting of the 5th floor slab', ''),
                ('Finishing stage', 25, 'When plaster and tiling begin', ''),
                ('On handover', 10, 'At the time of key handover', 'Includes utility deposits'),
            ]
            for i, (title, pct, timing, note) in enumerate(stages):
                PaymentStage.objects.create(project=p, title=title, share_pct=pct, timing=timing,
                                            note=note, order=i, status=True)

            # apartments
            Apartment.objects.filter(project=p).delete()
            for i, u in enumerate(d['units_data']):
                (unit_no, utype, title, size, beds, baths, balconies, parking,
                 facing, price, status) = u
                price_psf = (int(price / size) if price and size and d['category'] != 'land'
                             else (int(price / size) if price and size else None))
                apt = Apartment.objects.create(
                    project=p, unit_no=unit_no, floor_no=f'{max(2, i + 2)}',
                    unit_type=utype, title=title, size_sft=int(size),
                    beds=beds or 0, baths=baths or 0, balconies=balconies or 0,
                    parking=parking or 0, facing=facing, price=price,
                    price_per_sqft=price_psf, status=status, order=i,
                    note='' if status == 'available' else 'Please ask the desk about resale options.')
                apt.features.set(features[:6])
                load_plan(apt.floor_plan, 'floor-type-a.svg' if i % 2 == 0 else 'floor-type-b.svg')
                apt.save()

        # a couple of sample booking requests
        if not Booking.objects.exists():
            Booking.objects.create(
                project=Project.objects.filter(slug='sti-royal-tower').first(),
                kind='visit', full_name='Rifat Hossain', phone='01711000000',
                email='rifat@example.com', preferred_date=today + dt.timedelta(days=3),
                preferred_time='11:00 AM', budget='1.5 – 3 Cr',
                message='Would like to see the 3-bedroom corner unit with my family.')
            Booking.objects.create(
                project=Project.objects.filter(slug='sti-gulshan-prive').first(),
                kind='brochure', full_name='Nusrat Jahan', phone='01811000000',
                status='contacted', message='Please send the penthouse brochure and payment plan.')

    def services(self):
        data = [
            ('Apartment development', 'building',
             'Land acquisition, design, approval, construction and handover as a single contract.',
             'proj-gulshan.jpg'),
            ('Land sharing & joint venture', 'layers',
             'We fund and build on your land, and hand back a share of the finished apartments.',
             'proj-purbachal.jpg'),
            ('Commercial & mixed-use', 'office',
             'Grade-A office floors and mixed-use buildings designed for institutional tenants.',
             'proj-banani.jpg'),
            ('Interior & fit-out', 'lounge',
             'Turnkey interiors — design, procurement and execution by our own studio team.',
             'interior-kitchen.jpg'),
            ('Structural engineering', 'ruler',
             'In-house structural design to BNBC 2020, with third-party peer review.',
             'constr-1.jpg'),
            ('Post-handover care', 'shield',
             'Three-year maintenance desk, snag resolution and property management services.',
             'proj-dhanmondi.jpg'),
        ]
        for i, (title, icon, summary, image) in enumerate(data):
            s, _ = Service.objects.get_or_create(title=title)
            s.icon = icon
            s.summary = summary
            s.order = i
            s.status = True
            s.body = (f'<p>{summary}</p><p>Every stage is delivered by our own team and documented '
                      f'for the client: drawings, approvals, material approvals, progress reports and '
                      f'a final snag list signed off by both sides.</p><ul>'
                      f'<li>Feasibility and cost study before commitment</li>'
                      f'<li>Single point of accountability from design to handover</li>'
                      f'<li>Monthly reporting with photographs and cost tracking</li></ul>')
            attach(s.image, image)
            s.save()

    def team(self):
        data = [
            ('Md. Eshaq Ali', 'Managing Director', 'proj-gulshan.jpg'),
            ('Farhana Rahman', 'Director, Sales & Marketing', 'proj-dhanmondi.jpg'),
            ('Architect Tanvir Hasan', 'Head of Design', 'proj-banani.jpg'),
            ('Engr. Shahidul Islam', 'Chief Structural Engineer', 'constr-1.jpg'),
        ]
        for i, (name, role, img) in enumerate(data):
            t, _ = TeamMember.objects.get_or_create(name=name)
            t.designation = role
            t.order = i
            t.is_leadership = True
            t.status = True
            t.bio = (f'{name} leads {role.lower()} at STI Builders. '
                     f'Available for client meetings at the Uttara sales gallery.')
            attach(t.photo, img)
            t.save()

    def faqs(self):
        data = [
            ('Buying', 'How do I book an apartment?',
             '<p>Choose a project, select an available unit and submit a reservation through the '
             'booking page. The booking amount is refundable for seven days. Our desk then prepares '
             'the buyer agreement, payment schedule and registration papers.</p>'),
            ('Buying', 'What is included in the price?',
             '<p>The quoted price covers the apartment as per the finishing specification. '
             'Registration, utility connections, car parking (where charged separately) and '
             'service charges for the first year are additional and listed in the payment plan.</p>'),
            ('Buying', 'Can I use bank financing?',
             '<p>Yes. We work with most scheduled banks in Bangladesh and can share the approved '
             'project documents required for a mortgage. Our documentation desk assists with the '
             'bank file at no extra cost.</p>'),
            ('Buying', 'What warranty comes with the building?',
             '<p>Ten years on the structural frame, five years on waterproofing and two years on '
             'finishing. The warranty is written into the buyer agreement, not just the brochure.</p>'),
            ('Booking', 'Can I visit the site during construction?',
             '<p>Yes — site visits are arranged every Saturday and Wednesday. You will be given a '
             'safety briefing, a helmet and a walkthrough with the site engineer.</p>'),
            ('Booking', 'What happens if handover is delayed?',
             '<p>The agreement includes a delay clause: we pay a monthly compensation to the buyer '
             'for every month beyond the committed handover date, except where the delay is caused '
             'by force majeure or a change requested by the buyer.</p>'),
            ('Land sharing', 'Who pays for approvals and construction?',
             '<p>STI Builders funds RAJUK approval, design, construction and utility connections. '
             'The land owner contributes the land and does not need to raise capital.</p>'),
            ('Land sharing', 'How is the share decided?',
             '<p>The split depends on plot size, road width, allowable FAR and the condition of the '
             'title. Typical agreements range from 50:50 to 55:45 on net sellable area, fixed in '
             'the deed before construction begins.</p>'),
            ('Land sharing', 'Who gets their apartments first?',
             '<p>The land owner’s share is handed over first at completion — this is written into '
             'the deed. Registration and mutation costs for the owner’s units are borne by us.</p>'),
            ('Land sharing', 'What if I want to sell my share later?',
             '<p>You may sell at any time. We offer a first right of refusal and can list the units '
             'through our own sales desk.</p>'),
        ]
        for i, (group, q, a) in enumerate(data):
            f, _ = Faq.objects.get_or_create(question=q)
            f.answer = a
            f.group = group
            f.order = i
            f.status = True
            f.save()

    def testimonials(self):
        data = [
            ('Rezaul Karim', 'Flat owner, Royal Tower', 'sti-royal-tower',
             'The handover happened on the date written in the agreement, and the finishing was '
             'better than the brochure render. Four years in, the building still feels new.'),
            ('Shahnaz Parvin', 'Land owner, Purbachal', 'sti-purbachal-green-plots',
             'Their engineers walked me through every drawing before I signed the deed. Nothing '
             'was hidden, and the share they promised is the share I received.'),
            ('Ahmed Sajid', 'Investor, Gulshan Prive', 'sti-gulshan-prive',
             'I bought from overseas. The documentation desk handled the power of attorney and '
             'bank remittance, and the letting team found a tenant in three weeks.'),
            ('Nusrat Jahan', 'Resident, Lake Drive Paradise', 'sti-lake-drive-paradise',
             'Two years in and the maintenance team actually answers the phone. That is rarer in '
             'Dhaka than the lake view.'),
            ('Kamrul Hasan', 'Tenant, Banani Business Square', 'sti-banani-business-square',
             'Column-free floor plates and a lift bank that actually works in a power cut. Our '
             'team moved in without a single fit-out surprise.'),
            ('Sabrina Akter', 'Flat owner, Dhanmondi Court', 'sti-dhanmondi-court',
             'Only two families per floor. We know our neighbours, the balcony is genuinely deep, '
             'and the street is quiet at night.'),
        ]
        for i, (name, role, slug, quote) in enumerate(data):
            t, _ = Testimonial.objects.get_or_create(name=name, defaults={'quote': quote})
            t.role = role
            t.quote = quote
            t.project = Project.objects.filter(slug=slug).first()
            t.rating = 5
            t.order = i
            t.status = True
            t.save()

    def news(self):
        data = [
            ('STI Royal Tower reaches 8th floor slab, two months ahead of schedule',
             'news', 'sti-royal-tower',
             'The structural frame of Royal Tower has reached level eight, putting the project two '
             'months ahead of its committed handover curve.',
             'proj-gulshan.jpg', 3),
            ('Gulshan Prive handed over to all twelve owners',
             'news', 'sti-gulshan-prive',
             'Twelve families received their keys in a single week, with every snag closed before '
             'handover.', 'hero-tower.jpg', 4),
            ('Land sharing explained: what a fair deed looks like',
             'insight', None,
             'A plain-language walkthrough of the clauses a land owner should insist on before '
             'signing a development agreement in Dhaka.', 'proj-purbachal.jpg', 6),
            ('Why we publish our construction milestones',
             'blog', 'sti-lake-drive-paradise',
             'Monthly milestone reporting is not marketing — it is the cheapest insurance a buyer '
             'can have.', 'constr-1.jpg', 5),
            ('Purbachal plots: road frontage is the whole investment',
             'insight', 'sti-purbachal-green-plots',
             'Two plots of the same size can differ in value by forty percent based on the road '
             'they open onto. Here is how we price it.', 'land-1.jpg', 7),
            ('Our 2025 community health camp in Uttara',
             'event', None,
             'Free health screening for 400 residents across our handed-over buildings, in '
             'partnership with a local hospital.', 'csr-1.jpg', 2),
        ]
        for i, (title, kind, slug, excerpt, cover, mins) in enumerate(data):
            n, _ = NewsPost.objects.get_or_create(title=title)
            n.kind = kind
            n.excerpt = excerpt
            n.cover.name = ''
            attach(n.cover, cover)
            n.project = Project.objects.filter(slug=slug).first() if slug else None
            n.published_at = timezone.now().date() - dt.timedelta(days=i * 9 + 2)
            n.read_minutes = mins
            n.status = True
            n.body = (f'<p>{excerpt}</p><p>Full reporting from our site team, with photographs '
                      f'and the engineer’s notes, is shared with registered buyers every month. '
                      f'If you would like the latest report for a specific project, ask the desk '
                      f'and we will send it the same day.</p>'
                      f'<p>Milestone reporting covers structure, brickwork, plaster, tiling, '
                      f'lift installation and utility connections — each with a percentage and a '
                      f'date, so that a buyer can compare the promise with the progress.</p>')
            n.save()

    def gallery(self):
        items = [
            ('csr-1.jpg', 'Health camp for residents, Uttara', 'csr'),
            ('csr-2.jpg', 'Community screening day', 'csr'),
            ('csr-3.jpg', 'Handover ceremony', 'handover'),
            ('int-1.jpg', 'Living room, Gulshan Prive', 'interior'),
            ('int-2.jpg', 'Lobby detail, Royal Tower', 'interior'),
            ('int-3.jpg', 'Dining, Lake Drive Paradise', 'interior'),
            ('constr-1.jpg', 'Structural frame, Uttara Central', 'construction'),
            ('proj-uttara.jpg', 'Uttara Central under construction', 'construction'),
            ('proj-royal-2.jpg', 'Textile Palace at completion', 'handover'),
            ('proj-dhanmondi-2.jpg', 'Dhanmondi Court facade', 'handover'),
            ('villa-pool.jpg', 'Roof deck, Bashundhara', 'construction'),
            ('land-1.jpg', 'Purbachal plot development', 'construction'),
        ]
        for i, (img, caption, group) in enumerate(items):
            g, _ = GalleryImage.objects.get_or_create(caption=caption)
            attach(g.image, img)
            g.group = group
            g.order = i
            g.status = True
            g.save()
