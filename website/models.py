"""Models for the STI Builders public website.

The models here are intentionally self-contained so that the front-end (project
listings, project detail pages, apartment units, land-sharing breakdown, booking
system, construction milestones, insights...) can be driven entirely from the
Django admin without touching the legacy ``property`` / ``realstateapp`` apps.
"""
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def unique_slug(model, value, slug_field='slug', extra=''):
    base = slugify(value)[:180] or 'item'
    candidate = f'{base}-{extra}' if extra else base
    counter = 2
    while model.objects.filter(**{slug_field: candidate}).exists():
        candidate = f'{candidate}-{counter}'
        counter += 1
    return candidate


def money(value):
    """Bengali style grouping (1,25,00,000)."""
    if value is None:
        return ''
    try:
        value = int(round(float(value)))
    except (TypeError, ValueError):
        return str(value)
    s = str(abs(value))
    if len(s) <= 3:
        out = s
    else:
        last3, rest = s[-3:], s[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        out = ','.join(parts) + ',' + last3
    return ('-' if value < 0 else '') + out


# ---------------------------------------------------------------------------
# taxonomy
# ---------------------------------------------------------------------------
class Location(models.Model):
    """A suburb / area — also carries the analytics & insights shown on the site."""
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    city = models.CharField(max_length=120, default='Dhaka')
    zone = models.CharField(max_length=160, blank=True, help_text='e.g. North Dhaka')
    short_note = models.CharField(max_length=250, blank=True)
    description = RichTextField(blank=True)
    cover_image = models.ImageField(upload_to='website/locations', blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # suburb analytics
    avg_price_per_sqft = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True,
                                             help_text='Average BDT per sq ft')
    price_growth_yoy = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                           help_text='% price growth in the last 12 months')
    rental_yield = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                       help_text='% gross rental yield')
    demand_index = models.PositiveSmallIntegerField(default=0, help_text='0-100 buyer demand index')
    livability_score = models.PositiveSmallIntegerField(default=0, help_text='0-100 livability score')
    commute_minutes = models.PositiveSmallIntegerField(blank=True, null=True,
                                                       help_text='Average commute to Motijheel (minutes)')
    schools_count = models.PositiveSmallIntegerField(default=0)
    hospitals_count = models.PositiveSmallIntegerField(default=0)
    malls_count = models.PositiveSmallIntegerField(default=0)
    green_space_pct = models.PositiveSmallIntegerField(default=0, help_text='% of area that is green / open')
    highlight_1 = models.CharField(max_length=160, blank=True)
    highlight_2 = models.CharField(max_length=160, blank=True)
    highlight_3 = models.CharField(max_length=160, blank=True)
    road_access = models.CharField(max_length=160, blank=True, help_text='e.g. 40 ft + 60 ft road')
    status = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Suburb / Location'
        verbose_name_plural = 'Suburbs & Locations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(Location, self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('website:suburb_detail', args=[self.slug])


class Landmark(models.Model):
    """Nearby landmark shown on the project "Locations & Landmarks" tab."""
    CATEGORIES = [
        ('metro', 'Metro Rail Station'),
        ('school', 'School & University'),
        ('hospital', 'Hospital'),
        ('mall', 'Shopping & Dining'),
        ('park', 'Park & Lake'),
        ('airport', 'Airport'),
        ('office', 'Business District'),
        ('other', 'Other'),
    ]
    location = models.ForeignKey(Location, related_name='landmarks', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='other')
    distance_km = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    drive_minutes = models.PositiveSmallIntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('distance_km', 'order', 'name')
        verbose_name = 'Landmark'
        verbose_name_plural = 'Landmarks'

    def __str__(self):
        return f'{self.name} ({self.location.name})'


class Amenity(models.Model):
    ICONS = [
        ('pool', 'Swimming Pool'), ('gym', 'Gym'), ('parking', 'Parking'), ('lift', 'Elevator'),
        ('generator', 'Generator & IPS'), ('security', '24/7 Security'), ('cctv', 'CCTV'),
        ('roof', 'Roof Garden'), ('lounge', 'Community Lounge'), ('play', 'Kids Play Area'),
        ('mosque', 'Prayer Space'), ('garden', 'Landscaped Garden'), ('water', 'Water Treatment'),
        ('fire', 'Fire Fighting'), ('wifi', 'Community Wi-Fi'), ('club', 'Club House'),
        ('power', 'Power Sub-station'), ('intercom', 'Intercom'), ('laundry', 'Laundry'),
        ('ev', 'EV Charging'),
    ]
    name = models.CharField(max_length=160)
    icon = models.CharField(max_length=20, choices=ICONS, default='pool')
    note = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name


class Feature(models.Model):
    """Interior / construction feature (used on unit + project detail pages)."""
    name = models.CharField(max_length=160)
    status = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Feature'
        verbose_name_plural = 'Apartment Features'

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------
# projects
# ---------------------------------------------------------------------------
class ProjectQuerySet(models.QuerySet):
    def live(self):
        return self.filter(status=True, published=True)

    def by_stage(self, stage):
        return self.filter(stage=stage)

    def featured(self):
        return self.filter(featured=True)


class Project(models.Model):
    STAGE = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('handover', 'Handed Over'),
        ('ready', 'Ready to Move'),
    ]
    CATEGORY = [
        ('residential', 'Residential Apartment'),
        ('commercial', 'Commercial'),
        ('mixed', 'Mixed Use'),
        ('land', 'Plot & Land Sharing'),
    ]
    OWNERSHIP = [
        ('freehold', 'Freehold'),
        ('landshare', 'Land Sharing'),
        ('joint', 'Joint Venture'),
    ]

    # identity -------------------------------------------------------------
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    tagline = models.CharField(max_length=250, blank=True)
    code = models.CharField(max_length=40, blank=True, help_text='Internal ref, e.g. STI-014')
    category = models.CharField(max_length=20, choices=CATEGORY, default='residential')
    stage = models.CharField(max_length=20, choices=STAGE, default='ongoing', db_index=True)
    ownership = models.CharField(max_length=20, choices=OWNERSHIP, default='freehold')

    location = models.ForeignKey(Location, related_name='projects', on_delete=models.PROTECT)
    address = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=400, blank=True)
    description = RichTextField(blank=True)
    concept_note = models.TextField(blank=True, help_text='Design concept / architect statement')

    # hero + cards ---------------------------------------------------------
    cover_image = models.ImageField(upload_to='website/projects', blank=True)
    night_image = models.ImageField(upload_to='website/projects', blank=True,
                                    help_text='Optional hover image, usually a night view')
    hero_video_url = models.URLField(blank=True, help_text='MP4 / YouTube link for the hero')
    logo = models.ImageField(upload_to='website/projects/logos', blank=True)

    # building info --------------------------------------------------------
    land_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                    help_text='Land size in katha')
    land_area_unit = models.CharField(max_length=20, default='katha')
    floors = models.PositiveSmallIntegerField(blank=True, null=True)
    basement_levels = models.PositiveSmallIntegerField(default=0)
    total_units = models.PositiveSmallIntegerField(blank=True, null=True)
    units_per_floor = models.PositiveSmallIntegerField(blank=True, null=True)
    lifts = models.PositiveSmallIntegerField(default=0)
    staircases = models.PositiveSmallIntegerField(default=0)
    parking_spaces = models.PositiveSmallIntegerField(default=0)
    facing = models.CharField(max_length=80, blank=True)
    road_width = models.CharField(max_length=80, blank=True)
    plot_no = models.CharField(max_length=80, blank=True)
    block_no = models.CharField(max_length=80, blank=True)
    architect = models.CharField(max_length=200, blank=True)
    structural_consultant = models.CharField(max_length=200, blank=True)
    rajuk_number = models.CharField(max_length=120, blank=True)
    approval_authority = models.CharField(max_length=200, blank=True, default='RAJUK')
    handover_date = models.DateField(blank=True, null=True)
    launch_date = models.DateField(blank=True, null=True)
    completion_pct = models.PositiveSmallIntegerField(default=0, help_text='Overall construction progress %')

    # pricing --------------------------------------------------------------
    price_from = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    size_from = models.PositiveIntegerField(blank=True, null=True)
    size_to = models.PositiveIntegerField(blank=True, null=True)
    beds_from = models.PositiveSmallIntegerField(blank=True, null=True)
    beds_to = models.PositiveSmallIntegerField(blank=True, null=True)
    booking_amount = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)

    # relations ------------------------------------------------------------
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='projects')
    features = models.ManyToManyField(Feature, blank=True, related_name='projects')

    # location & map -------------------------------------------------------
    map_embed_url = models.TextField(blank=True, help_text='Google Maps embed src URL')
    map_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    map_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # brochure & media -----------------------------------------------------
    brochure = models.FileField(upload_to='website/brochures', blank=True)
    brochure_note = models.CharField(max_length=200, blank=True,
                                     help_text='e.g. PDF · 8.4 MB · Updated Nov 2025')
    video_1_url = models.URLField(blank=True, verbose_name='Walkthrough video')
    video_2_url = models.URLField(blank=True, verbose_name='Drone video')
    video_3_url = models.URLField(blank=True, verbose_name='Client testimonial video')

    # social ---------------------------------------------------------------
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    social_hashtag = models.CharField(max_length=80, blank=True, default='STIBuilders')

    # land sharing ---------------------------------------------------------
    land_owner_share = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                           help_text='% of built area given to the land owner')
    developer_share = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                          help_text='% of built area retained by STI Builders')
    land_share_note = models.TextField(blank=True)

    # flags ----------------------------------------------------------------
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ('order', '-created_at')
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(Project, self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('website:project_detail', args=[self.slug])

    # -- presentation helpers ---------------------------------------------
    @property
    def stage_label(self):
        return dict(self.STAGE).get(self.stage, self.stage)

    @property
    def category_label(self):
        return dict(self.CATEGORY).get(self.category, self.category)

    @property
    def ownership_label(self):
        return dict(self.OWNERSHIP).get(self.ownership, self.ownership)

    @property
    def price_display(self):
        """'৳ 1.25 Cr' style short price."""
        if not self.price_from:
            return 'On request'
        return short_bdt(self.price_from)

    @property
    def price_full(self):
        return f'BDT {money(self.price_from)}' if self.price_from else 'On request'

    @property
    def size_unit(self):
        return 'katha' if self.category == 'land' else 'sft'

    @property
    def price_unit(self):
        return 'katha' if self.category == 'land' else 'sft'

    @property
    def size_range(self):
        unit = self.size_unit
        if self.size_from and self.size_to and self.size_from != self.size_to:
            return f'{money(self.size_from)} – {money(self.size_to)} {unit}'
        if self.size_from:
            return f'{money(self.size_from)} {unit}'
        return ''

    @property
    def bed_range(self):
        if self.beds_from and self.beds_to and self.beds_from != self.beds_to:
            return f'{self.beds_from} – {self.beds_to} Beds'
        if self.beds_from:
            return f'{self.beds_from} Bed' if self.beds_from == 1 else f'{self.beds_from} Beds'
        return ''

    @property
    def days_to_handover(self):
        if not self.handover_date:
            return None
        delta = (self.handover_date - timezone.now().date()).days
        return delta if delta > 0 else 0

    @property
    def stage_progress(self):
        """Progress used by the vertical progress rail on cards / details."""
        if self.stage == 'handover':
            return 100
        if self.stage == 'ready':
            return 100
        if self.stage == 'upcoming':
            return min(self.completion_pct, 15)
        return max(5, min(self.completion_pct or 45, 99))

    @property
    def map_src(self):
        if self.map_embed_url:
            return self.map_embed_url
        if self.map_latitude and self.map_longitude:
            return (f'https://maps.google.com/maps?q={self.map_latitude},{self.map_longitude}'
                    '&z=15&output=embed')
        if self.location.latitude and self.location.longitude:
            return (f'https://maps.google.com/maps?q={self.location.latitude},{self.location.longitude}'
                    '&z=14&output=embed')
        query = (self.address or self.location.name).replace(' ', '+')
        return f'https://maps.google.com/maps?q={query}&z=14&output=embed'

    @property
    def videos(self):
        out = []
        for url, label in ((self.video_1_url, 'Walkthrough'), (self.video_2_url, 'Drone'),
                           (self.video_3_url, 'Client Story')):
            if url:
                out.append({'url': url, 'label': label, 'embed': video_embed(url)})
        return out

    @property
    def gallery(self):
        return list(self.images.filter(status=True).order_by('order', 'id'))

    @property
    def next_milestone(self):
        return self.milestones.filter(status=True, is_done=False).order_by('order', 'target_date').first()

    @property
    def primary_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        return ''


class ProjectImage(models.Model):
    CATEGORY = [
        ('exterior', 'Exterior'),
        ('interior', 'Interior'),
        ('amenity', 'Amenity'),
        ('construction', 'Construction'),
        ('plan', 'Plan & Drawing'),
        ('location', 'Location'),
    ]
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='website/projects/gallery')
    caption = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY, default='exterior')
    is_cover = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Gallery'

    def __str__(self):
        return f'{self.project.name} — {self.caption or self.get_category_display()}'


class ProjectFloorPlan(models.Model):
    """Design & drawings tab."""
    KIND = [
        ('floor', 'Typical Floor Plan'),
        ('unit', 'Unit Plan'),
        ('site', 'Site Plan'),
        ('elevation', 'Elevation'),
        ('section', 'Section'),
        ('master', 'Master Plan'),
        ('3d', '3D Visual'),
    ]
    project = models.ForeignKey(Project, related_name='floor_plans', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=20, choices=KIND, default='floor')
    image = models.ImageField(upload_to='website/projects/plans', blank=True)
    drawing_file = models.FileField(upload_to='website/projects/drawings', blank=True)
    area_sft = models.PositiveIntegerField(blank=True, null=True)
    beds = models.PositiveSmallIntegerField(blank=True, null=True)
    baths = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Drawing / Floor Plan'
        verbose_name_plural = 'Design & Drawings'

    def __str__(self):
        return f'{self.project.name} — {self.title}'


class Milestone(models.Model):
    """Project milestones / construction stages with a percentage."""
    project = models.ForeignKey(Project, related_name='milestones', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, blank=True)
    target_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    progress_pct = models.PositiveSmallIntegerField(default=0)
    is_done = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'target_date', 'id')
        verbose_name = 'Milestone / Stage'
        verbose_name_plural = 'Milestones & Stages'

    def __str__(self):
        return f'{self.project.name} — {self.title}'


class PaymentStage(models.Model):
    """Used by the land-sharing breakdown & the payment schedule."""
    project = models.ForeignKey(Project, related_name='payment_stages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    share_pct = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                    help_text='% of the total consideration')
    timing = models.CharField(max_length=200, blank=True, help_text='e.g. On signing the deed')
    note = models.CharField(max_length=300, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Payment / Share Stage'
        verbose_name_plural = 'Payment & Share Breakdown'

    def __str__(self):
        return f'{self.project.name} — {self.title}'


class Apartment(models.Model):
    """An individual apartment / flat type offered in a project."""
    STATUS = [
        ('available', 'Available'),
        ('hold', 'On Hold'),
        ('booked', 'Booked'),
        ('sold', 'Sold Out'),
    ]
    UNIT_TYPE = [
        ('2bed', '2 Bedroom'), ('3bed', '3 Bedroom'), ('4bed', '4 Bedroom'),
        ('5bed', '5 Bedroom / Duplex'), ('studio', 'Studio'),
        ('office', 'Office Space'), ('shop', 'Retail / Shop'),
        ('plot', 'Residential Plot'),
    ]
    project = models.ForeignKey(Project, related_name='apartments', on_delete=models.CASCADE)
    unit_no = models.CharField(max_length=40, blank=True)
    floor_no = models.CharField(max_length=40, blank=True)
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPE, default='3bed')
    title = models.CharField(max_length=160, blank=True, help_text='e.g. Type A — Corner')
    size_sft = models.PositiveIntegerField(default=0)
    balcony_sft = models.PositiveIntegerField(default=0, blank=True, null=True)
    beds = models.PositiveSmallIntegerField(default=3)
    baths = models.PositiveSmallIntegerField(default=3)
    balconies = models.PositiveSmallIntegerField(default=1)
    parking = models.PositiveSmallIntegerField(default=1)
    facing = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='available')
    features = models.ManyToManyField(Feature, blank=True, related_name='apartments')
    floor_plan = models.ImageField(upload_to='website/units/plans', blank=True)
    note = models.CharField(max_length=300, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'size_sft', 'id')
        verbose_name = 'Apartment / Flat'
        verbose_name_plural = 'Apartments & Flats'

    def __str__(self):
        return f'{self.project.name} — {self.title or self.unit_no or self.get_unit_type_display()}'

    @property
    def area_unit(self):
        return 'katha' if self.unit_type == 'plot' else 'sft'

    @property
    def size_label(self):
        return f'{money(self.size_sft)} {self.area_unit}'

    @property
    def label(self):
        return self.title or f'{self.get_unit_type_display()} · {self.size_label}'

    @property
    def status_label(self):
        return self.get_status_display()

    @property
    def price_display(self):
        return short_bdt(self.price) if self.price else 'On request'

    @property
    def availability(self):
        return 'Available' if self.status == 'available' else self.get_status_display()

    @property
    def is_available(self):
        return self.status == 'available'

    @property
    def plan_image(self):
        """Floor plan to show, falling back to the project's typical plan."""
        if self.floor_plan:
            return self.floor_plan.url
        for plan in self.project.floor_plans.all():
            if plan.image:
                return plan.image.url
        return None

    @property
    def schedule_base(self):
        """Price the payment schedule is calculated from.

        Sold units often have no listed price, but a buyer still wants to know
        how a flat at this size is paid for, so fall back to the project entry
        price rather than showing nothing.
        """
        return self.price or self.project.price_from

    @property
    def pricing_is_projected(self):
        return not self.price and bool(self.project.price_from)

    @property
    def pricing(self):
        """Construction-linked payment schedule derived from the unit price.

        Percentages follow the usual Bangladeshi apartment convention: a
        booking deposit, then stage payments tied to the physical build.
        """
        base = self.schedule_base
        if not base:
            return []
        stages = [
            ('Booking money', 10, 'On signing the allotment letter'),
            ('Agreement & handover of documents', 15, 'Within 30 days of booking'),
            ('Piling & foundation complete', 15, 'Structural start on site'),
            ('Ground floor slab cast', 10, 'Superstructure begins'),
            ('Typical floors cast', 25, 'Apportioned across floors'),
            ('Roof slab & brickwork', 10, 'Building watertight'),
            ('Finishing & fittings', 10, 'Tiles, paint, joinery'),
            ('Handover', 5, 'On keys and completion certificate'),
        ]
        out = []
        for name, pct, note in stages:
            amount = int(base) * pct // 100
            out.append({'name': name, 'pct': pct, 'amount': amount, 'note': note})
        return out

    @property
    def booking_amount(self):
        if not self.schedule_base:
            return None
        return int(self.schedule_base) // 10

    @property
    def size_per_bed(self):
        if not self.beds:
            return None
        return round(self.size_sft / self.beds)

    @property
    def features_by_group(self):
        """Features grouped for display, so the page reads as sections."""
        groups = {}
        for feature in self.features.all():
            groups.setdefault(feature.get_group_display() if hasattr(feature, 'get_group_display') else 'Features', []).append(feature)
        return groups


class Booking(models.Model):
    """Site-visit / unit booking request collected from the public site."""
    STATUS = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('visit', 'Site Visit Scheduled'),
        ('negotiation', 'In Negotiation'),
        ('booked', 'Booked'),
        ('closed', 'Closed'),
    ]
    KIND = [
        ('visit', 'Book a Site Visit'),
        ('reserve', 'Reserve an Apartment'),
        ('call', 'Request a Call Back'),
        ('brochure', 'Request Brochure'),
    ]
    reference = models.CharField(max_length=24, unique=True, blank=True)
    project = models.ForeignKey(Project, related_name='bookings', on_delete=models.SET_NULL,
                                blank=True, null=True)
    apartment = models.ForeignKey(Apartment, related_name='bookings', on_delete=models.SET_NULL,
                                  blank=True, null=True)
    kind = models.CharField(max_length=20, choices=KIND, default='visit')
    full_name = models.CharField(max_length=160)
    phone = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    preferred_date = models.DateField(blank=True, null=True)
    preferred_time = models.CharField(max_length=40, blank=True)
    budget = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Booking Request'
        verbose_name_plural = 'Booking Requests'

    def __str__(self):
        return f'{self.reference} · {self.full_name}'

    def save(self, *args, **kwargs):
        if not self.reference:
            stamp = timezone.now().strftime('%y%m%d')
            count = Booking.objects.filter(created_at__date=timezone.now().date()).count() + 1
            self.reference = f'STI-{stamp}-{count:03d}'
        super().save(*args, **kwargs)


class Enquiry(models.Model):
    """General contact / consultation enquiry."""
    SUBJECTS = [
        ('buy', 'Buying an Apartment'),
        ('land', 'Land Sharing Proposal'),
        ('invest', 'Investment & NRI Desk'),
        ('career', 'Career'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=160)
    phone = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=20, choices=SUBJECTS, default='buy')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='enquiries')
    message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f'{self.name} — {self.get_subject_display()}'


# ---------------------------------------------------------------------------
# editorial / corporate content
# ---------------------------------------------------------------------------
class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    icon = models.CharField(max_length=40, default='building')
    summary = models.CharField(max_length=300, blank=True)
    body = RichTextField(blank=True)
    image = models.ImageField(upload_to='website/services', blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'title')
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(Service, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('website:service_detail', args=[self.slug])


class TeamMember(models.Model):
    name = models.CharField(max_length=160)
    designation = models.CharField(max_length=160)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='website/team', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    linkedin_url = models.URLField(blank=True)
    is_leadership = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Team Member'
        verbose_name_plural = 'Management Team'

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=160)
    role = models.CharField(max_length=160, blank=True, help_text='e.g. Flat owner, Royal Tower')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='testimonials')
    quote = models.TextField()
    photo = models.ImageField(upload_to='website/testimonials', blank=True)
    rating = models.PositiveSmallIntegerField(default=5)
    is_video = models.BooleanField(default=False)
    video_url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class NewsPost(models.Model):
    KIND = [('news', 'Company News'), ('press', 'Press'), ('event', 'Event'), ('blog', 'Insight')]
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=260, unique=True, blank=True)
    kind = models.CharField(max_length=20, choices=KIND, default='news')
    excerpt = models.CharField(max_length=400, blank=True)
    body = RichTextField(blank=True)
    cover = models.ImageField(upload_to='website/news', blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='posts')
    published_at = models.DateField(default=timezone.now)
    read_minutes = models.PositiveSmallIntegerField(default=4)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-published_at', '-id')
        verbose_name = 'News / Insight'
        verbose_name_plural = 'News & Insights'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(NewsPost, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('website:news_detail', args=[self.slug])


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = RichTextField(blank=True)
    group = models.CharField(max_length=80, default='Buying', help_text='Buying / Land Sharing / Booking')
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class GalleryImage(models.Model):
    GROUP = [('construction', 'Construction'), ('interior', 'Interior'),
             ('csr', 'CSR & Events'), ('handover', 'Handover'), ('office', 'Office')]
    image = models.ImageField(upload_to='website/gallery')
    caption = models.CharField(max_length=200, blank=True)
    group = models.CharField(max_length=20, choices=GROUP, default='construction')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='gallery_images')
    order = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.caption or f'Gallery #{self.pk}'


class SiteSetting(models.Model):
    """Singleton-ish site wide settings edited from the admin."""
    company_name = models.CharField(max_length=160, default='STI Builders Limited')
    tagline = models.CharField(max_length=250, blank=True)
    logo = models.ImageField(upload_to='website/site', blank=True)
    logo_light = models.ImageField(upload_to='website/site', blank=True,
                                   help_text='White version used on the dark navbar/footer')
    phone = models.CharField(max_length=40, blank=True)
    phone_2 = models.CharField(max_length=40, blank=True)
    hotline = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    sales_email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    office_hours = models.CharField(max_length=160, blank=True)
    whatsapp = models.CharField(max_length=40, blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    map_embed_url = models.TextField(blank=True)
    about_short = models.TextField(blank=True)
    years_experience = models.PositiveSmallIntegerField(default=12)
    projects_delivered = models.PositiveSmallIntegerField(default=24)
    happy_families = models.PositiveSmallIntegerField(default=1800)
    sqft_delivered = models.PositiveIntegerField(default=2200000)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.company_name

    @classmethod
    def get(cls):
        return cls.objects.first() or cls()


# ---------------------------------------------------------------------------
# small helpers used by templates / models
# ---------------------------------------------------------------------------
def short_bdt(value):
    """1.25 Cr / 78.5 Lac / ৳ 45,000 style formatting."""
    if value is None:
        return 'On request'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if value >= 10000000:
        return f'৳ {value / 10000000:.2f} Cr'
    if value >= 100000:
        return f'৳ {value / 100000:.1f} Lac'
    if value >= 1000:
        return f'৳ {value / 1000:.0f}K'
    return f'৳ {value:.0f}'


def video_embed(url):
    """Return (kind, src) tuple for a video URL."""
    if not url:
        return None
    url = url.strip()
    if 'youtube.com/watch' in url:
        vid = url.split('v=')[-1].split('&')[0]
        return f'https://www.youtube.com/embed/{vid}'
    if 'youtu.be/' in url:
        return f'https://www.youtube.com/embed/{url.split("youtu.be/")[-1].split("?")[0]}'
    if 'vimeo.com/' in url:
        return f'https://player.vimeo.com/video/{url.rstrip("/").split("/")[-1]}'
    if 'facebook.com' in url:
        return f'https://www.facebook.com/plugins/video.php?href={url}&show_text=false'
    return url
