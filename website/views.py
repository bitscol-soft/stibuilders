"""Public-facing views for the STI Builders website."""
import json
from decimal import Decimal

from django.contrib import messages
from django.db.models import Count, Min, Max, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import (Amenity, Apartment, Booking, Enquiry, Faq, GalleryImage, Landmark,
                     Location, Milestone, NewsPost, Project, Service, SiteSetting,
                     TeamMember, Testimonial, money, short_bdt)


# ---------------------------------------------------------------------------
# shared context
# ---------------------------------------------------------------------------
def site_context():
    setting = SiteSetting.get()
    return {
        'site': setting,
        'nav_locations': Location.objects.filter(status=True)[:8],
        'nav_amenities': Amenity.objects.filter(status=True)[:16],
        'footer_projects': Project.objects.live().order_by('order')[:5],
        'footer_services': Service.objects.filter(status=True)[:5],
        'stage_counts': {
            'all': Project.objects.live().count(),
            'upcoming': Project.objects.live().filter(stage='upcoming').count(),
            'ongoing': Project.objects.live().filter(stage='ongoing').count(),
            'handover': Project.objects.live().filter(stage='handover').count(),
            'ready': Project.objects.live().filter(stage='ready').count(),
        },
    }


def project_queryset():
    return (Project.objects.live()
            .select_related('location')
            .prefetch_related('images', 'apartments', 'milestones'))


# ---------------------------------------------------------------------------
# home
# ---------------------------------------------------------------------------
def home(request):
    projects = project_queryset()
    featured = projects.filter(featured=True)[:3] or projects[:3]
    ongoing = projects.filter(stage='ongoing')[:4]
    upcoming = projects.filter(stage='upcoming')[:3]
    handover = projects.filter(stage__in=['handover', 'ready'])[:3]
    locations = Location.objects.filter(status=True).annotate(
        project_total=Count('projects', filter=Q(projects__status=True, projects__published=True))
    )
    ctx = site_context()
    ctx.update({
        'featured_projects': featured,
        'ongoing_projects': ongoing,
        'upcoming_projects': upcoming,
        'handover_projects': handover,
        'locations': locations,
        'services': Service.objects.filter(status=True)[:6],
        'testimonials': Testimonial.objects.filter(status=True)[:6],
        'posts': NewsPost.objects.filter(status=True)[:3],
        'stats': insights_payload(),
        'amenities': Amenity.objects.filter(status=True)[:12],
        'hero_projects': projects.order_by('-featured', 'order')[:3],
        'total_units': Apartment.objects.filter(is_active=True, project__status=True).count(),
        'map_points': [{
            'name': p.name, 'slug': p.slug, 'url': p.get_absolute_url(),
            'lat': float(p.map_latitude or p.location.latitude or 23.8759),
            'lng': float(p.map_longitude or p.location.longitude or 90.3795),
            'stage': p.stage_label, 'stageKey': p.stage, 'price': p.price_full,
            'location': p.location.name,
            'image': p.cover_image.url if p.cover_image else '',
        } for p in projects],
    })
    return render(request, 'website/home.html', ctx)


def insights_payload():
    """Numbers used by the counter strip + suburb analytics chart."""
    agg = Project.objects.live().aggregate(
        min_price=Min('price_from'), max_price=Max('price_from'),
        min_size=Min('size_from'), max_size=Max('size_to'))
    suburbs = []
    for loc in Location.objects.filter(status=True)[:6]:
        suburbs.append({
            'name': loc.name,
            'price': float(loc.avg_price_per_sqft or 0),
            'growth': float(loc.price_growth_yoy or 0),
            'demand': loc.demand_index,
        })
    return {'agg': agg, 'suburbs': suburbs}


# ---------------------------------------------------------------------------
# project listing + filters
# ---------------------------------------------------------------------------
SORTS = {
    'featured': ('order', '-featured', '-created_at'),
    'newest': ('-created_at',),
    'price_low': ('price_from',),
    'price_high': ('-price_from',),
    'size_high': ('-size_to',),
    'handover': ('handover_date',),
    'popular': ('-views',),
}


def project_list(request):
    qs = project_queryset()

    stage = request.GET.get('stage', '').strip()
    category = request.GET.getlist('category')
    ownership = request.GET.get('ownership', '').strip()
    suburb = request.GET.getlist('suburb')
    beds = request.GET.get('beds', '').strip()
    price_min = request.GET.get('price_min', '').strip()
    price_max = request.GET.get('price_max', '').strip()
    size_min = request.GET.get('size_min', '').strip()
    size_max = request.GET.get('size_max', '').strip()
    amenity_ids = request.GET.getlist('amenity')
    q = request.GET.get('q', '').strip()
    availability = request.GET.get('availability', '').strip()
    sort = request.GET.get('sort', 'featured')

    if stage and stage != 'all':
        qs = qs.filter(stage=stage)
    if category:
        qs = qs.filter(category__in=category)
    if ownership:
        qs = qs.filter(ownership=ownership)
    if suburb:
        qs = qs.filter(location__slug__in=suburb)
    if beds:
        try:
            beds = int(beds)
            qs = qs.filter(Q(beds_to__gte=beds) | Q(apartments__beds__gte=beds)).distinct()
        except ValueError:
            pass
    if price_min:
        try:
            qs = qs.filter(price_from__gte=Decimal(price_min))
        except Exception:
            pass
    if price_max:
        try:
            qs = qs.filter(price_from__lte=Decimal(price_max))
        except Exception:
            pass
    if size_min:
        try:
            qs = qs.filter(size_to__gte=int(size_min))
        except Exception:
            pass
    if size_max:
        try:
            qs = qs.filter(size_from__lte=int(size_max))
        except Exception:
            pass
    if amenity_ids:
        qs = qs.filter(amenities__id__in=amenity_ids).distinct()
    if availability == 'available':
        qs = qs.filter(apartments__status='available').distinct()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(location__name__icontains=q) |
                       Q(address__icontains=q) | Q(tagline__icontains=q)).distinct()

    ordering = SORTS.get(sort, SORTS['featured'])
    qs = qs.order_by(*ordering)

    total_found = qs.count()
    page_size = 9
    try:
        page = max(1, int(request.GET.get('page', 1)))
    except ValueError:
        page = 1
    start = (page - 1) * page_size
    projects = list(qs[start:start + page_size])
    total_pages = max(1, (total_found + page_size - 1) // page_size)

    params = request.GET.copy()
    params.pop('page', None)

    ctx = site_context()
    ctx.update({
        'projects': projects,
        'total_found': total_found,
        'page': page,
        'total_pages': total_pages,
        'page_range': range(1, total_pages + 1),
        'query_string': params.urlencode(),
        'active_filters': {
            'stage': stage, 'category': category, 'ownership': ownership,
            'suburb': suburb, 'beds': beds, 'price_min': price_min,
            'price_max': price_max, 'size_min': size_min, 'size_max': size_max,
            'amenity': amenity_ids, 'q': q, 'sort': sort, 'availability': availability,
        },
        'filter_state': json.dumps({
            'stage': stage, 'category': category, 'ownership': ownership,
            'suburb': suburb, 'beds': str(beds or ''), 'price_min': price_min,
            'price_max': price_max, 'size_min': size_min, 'size_max': size_max,
            'amenity': amenity_ids, 'q': q, 'sort': sort, 'availability': availability,
        }),
        'locations': Location.objects.filter(status=True),
        'amenities': Amenity.objects.filter(status=True),
        'sort_options': [
            ('featured', 'Featured first'), ('newest', 'Newest arrivals'),
            ('price_low', 'Price: low to high'), ('price_high', 'Price: high to low'),
            ('size_high', 'Largest units'), ('handover', 'Handover soonest'),
            ('popular', 'Most viewed'),
        ],
        'price_bounds': {'min': 2500000, 'max': 50000000},
        'map_points': [
            {'name': p.name, 'slug': p.slug,
             'lat': float(p.map_latitude or p.location.latitude or 23.8759),
             'lng': float(p.map_longitude or p.location.longitude or 90.3795),
             'stage': p.stage_label, 'stageKey': p.stage, 'price': p.price_full,
             'location': p.location.name,
             'image': p.cover_image.url if p.cover_image else ''}
            for p in projects
        ],
    })
    return render(request, 'website/project_list.html', ctx)


def project_map_data(request):
    """JSON feed used by the listing map."""
    points = []
    for p in project_queryset():
        lat = p.map_latitude or p.location.latitude
        lng = p.map_longitude or p.location.longitude
        points.append({
            'name': p.name, 'slug': p.slug, 'stage': p.stage_label,
            'stageKey': p.stage, 'price': p.price_full, 'location': p.location.name,
            'lat': float(lat or 0), 'lng': float(lng or 0),
            'image': p.cover_image.url if p.cover_image else '',
            'url': p.get_absolute_url(), 'progress': p.stage_progress,
        })
    return JsonResponse({'projects': points})


# ---------------------------------------------------------------------------
# project detail
# ---------------------------------------------------------------------------
def project_detail(request, slug):
    project = get_object_or_404(project_queryset(), slug=slug)
    Project.objects.filter(pk=project.pk).update(views=project.views + 1)

    apartments = project.apartments.filter(is_active=True).prefetch_related('features')
    amenities = project.amenities.filter(status=True)
    features = project.features.filter(status=True)
    plans = project.floor_plans.filter(status=True)
    milestones = project.milestones.filter(status=True)
    gallery = project.images.filter(status=True)
    landmarks = project.location.landmarks.filter(status=True)

    similar = (Project.objects.live()
               .filter(location=project.location).exclude(pk=project.pk)[:3])
    if not similar:
        similar = Project.objects.live().exclude(pk=project.pk)[:3]

    ctx = site_context()
    ctx.update({
        'project': project,
        'apartments': apartments,
        'amenities': amenities,
        'features': features,
        'plans': plans,
        'milestones': milestones,
        'gallery': gallery,
        'landmarks': landmarks,
        'landmark_groups': _group_landmarks(landmarks),
        'similar': similar,
        'testimonials': Testimonial.objects.filter(status=True, project=project)[:3] or
                         Testimonial.objects.filter(status=True)[:3],
        'stage_progress': project.stage_progress,
        'unit_beds': sorted({a.beds for a in apartments}),
        'available_units': sum(1 for a in apartments if a.status == 'available'),
        'specs': _project_specs(project),
        'map_points': [{
            'name': project.name, 'slug': project.slug,
            'lat': float(project.map_latitude or project.location.latitude or 0),
            'lng': float(project.map_longitude or project.location.longitude or 0),
            'stage': project.stage_label, 'price': project.price_full,
            'image': project.cover_image.url if project.cover_image else '',
        }],
        'land_share': project.land_owner_share or 52,
        'dev_share': project.developer_share or 48,
        'is_saved': str(project.pk) in request.session.get('saved_projects', []),
    })
    return render(request, 'website/project_detail.html', ctx)


def _group_landmarks(landmarks):
    order = ['metro', 'school', 'hospital', 'mall', 'park', 'office', 'airport', 'other']
    labels = dict(Landmark.CATEGORIES)
    out = []
    for key in order:
        items = [l for l in landmarks if l.category == key]
        if items:
            out.append({'key': key, 'label': labels.get(key, key), 'items': items})
    return out


def _project_specs(project):
    return [
        ('Land area', f'{project.land_area} {project.land_area_unit}' if project.land_area else '—'),
        ('Floors', project.floors or '—'),
        ('Basement', f'{project.basement_levels} level(s)' if project.basement_levels else '—'),
        ('Total units', project.total_units or '—'),
        ('Units / floor', project.units_per_floor or '—'),
        ('Lifts', project.lifts or '—'),
        ('Staircases', project.staircases or '—'),
        ('Parking', f'{project.parking_spaces} cars' if project.parking_spaces else '—'),
        ('Facing', project.facing or '—'),
        ('Road width', project.road_width or '—'),
        ('Plot / Block', f'{project.plot_no or "—"} / {project.block_no or "—"}'),
        ('Architect', project.architect or '—'),
        ('Structural', project.structural_consultant or '—'),
        ('RAJUK approval', project.rajuk_number or '—'),
    ]


def apartment_modal(request, slug, pk):
    """HTMX fragment: apartment detail card."""
    project = get_object_or_404(Project, slug=slug)
    unit = get_object_or_404(Apartment, pk=pk, project=project)
    return render(request, 'website/includes/unit_modal.html',
                  {'unit': unit, 'project': project})


def apartment_detail(request, slug, pk):
    """A full page for one flat, not just a modal.

    Each apartment gets its own URL so it can be shared, linked from the search
    engine, and read on a phone without opening a dialog.
    """
    project = get_object_or_404(Project.objects.select_related('location'), slug=slug)
    unit = get_object_or_404(
        Apartment.objects.select_related('project', 'project__location')
        .prefetch_related('features'), pk=pk, project=project)
    siblings = list(project.apartments.filter(is_active=True)
                    .select_related('project').order_by('order', 'size_sft', 'id'))
    index = next((i for i, u in enumerate(siblings) if u.pk == unit.pk), None)
    similar = [u for u in siblings if u.pk != unit.pk][:3]

    milestones = project.milestones.all()
    floor_plan = unit.floor_plan or next(
        (p for p in project.floor_plans.all() if p.image), None)

    ctx = site_context()
    ctx.update({
        'project': project,
        'unit': unit,
        'similar': similar,
        'milestones': milestones,
        'floor_plan': floor_plan,
        'project_features': project.features.filter(status=True),
        # a feature already listed under the building spec is not repeated as a
        # unit-specific extra
        'unit_only_features': unit.features.exclude(
            pk__in=project.features.values('pk')),
        'landmarks': project.location.landmarks.all()[:6] if project.location else [],
        'prev_unit': siblings[index - 1] if index not in (None, 0) else None,
        'next_unit': siblings[index + 1] if index is not None and index + 1 < len(siblings) else None,
    })
    return render(request, 'website/apartment_detail.html', ctx)


def project_units_json(request, slug):
    project = get_object_or_404(Project, slug=slug)
    units = [{
        'id': a.pk, 'label': a.label, 'status': a.status, 'statusLabel': a.status_label,
        'size': a.size_sft, 'beds': a.beds, 'baths': a.baths, 'price': a.price_display,
    } for a in project.apartments.filter(is_active=True)]
    return JsonResponse({'units': units})


# ---------------------------------------------------------------------------
# suburbs
# ---------------------------------------------------------------------------
def suburb_list(request):
    locations = Location.objects.filter(status=True).annotate(
        project_total=Count('projects', filter=Q(projects__status=True, projects__published=True)),
        min_price=Min('projects__price_from', filter=Q(projects__status=True)),
    )
    ctx = site_context()
    ctx.update({'locations': locations,
                'suburbs': [{'name': l.name, 'price': float(l.avg_price_per_sqft or 0),
                             'growth': float(l.price_growth_yoy or 0),
                             'demand': l.demand_index} for l in locations]})
    return render(request, 'website/suburbs.html', ctx)


def suburb_detail(request, slug):
    location = get_object_or_404(Location.objects.filter(status=True), slug=slug)
    projects = project_queryset().filter(location=location)
    ctx = site_context()
    ctx.update({
        'location': location,
        'projects': projects,
        'landmarks': location.landmarks.filter(status=True),
        'landmark_groups': _group_landmarks(location.landmarks.filter(status=True)),
        'amenity_ids': list(location.projects.values_list('amenities__icon', flat=True)),
        'map_src': f'https://maps.google.com/maps?q={location.latitude},{location.longitude}&z=14&output=embed'
                   if location.latitude else '',
        'price_low': projects.order_by('price_from').first(),
        'price_high': projects.order_by('-price_from').first(),
        'others': Location.objects.filter(status=True).exclude(pk=location.pk)[:4],
    })
    return render(request, 'website/suburb_detail.html', ctx)


# ---------------------------------------------------------------------------
# booking + enquiries
# ---------------------------------------------------------------------------
def book_visit(request):
    projects = Project.objects.live()
    project = None
    unit = None
    if request.GET.get('project'):
        project = projects.filter(slug=request.GET.get('project')).first()
    if request.GET.get('unit'):
        unit = Apartment.objects.filter(pk=request.GET.get('unit')).first()

    if request.method == 'POST':
        data = request.POST

        def clean_int(value, model):
            try:
                return value if value and model.objects.filter(pk=value).exists() else None
            except (TypeError, ValueError):
                return None

        want_kind = data.get('kind', 'visit')
        if want_kind not in dict(Booking.KIND):
            want_kind = 'visit'
        booking = Booking.objects.create(
            project_id=clean_int(data.get('project'), Project),
            apartment_id=clean_int(data.get('apartment'), Apartment),
            kind=want_kind,
            full_name=data.get('full_name', '').strip() or 'Guest',
            phone=data.get('phone', '').strip(),
            email=data.get('email', '').strip(),
            preferred_date=data.get('preferred_date') or None,
            preferred_time=data.get('preferred_time', ''),
            budget=data.get('budget', ''),
            message=data.get('message', ''),
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'ok': True, 'reference': booking.reference})
        messages.success(request, f'Thank you — your booking reference is {booking.reference}. '
                                  'Our sales desk will call you within one business day.')
        return redirect(f'/booking/?ref={booking.reference}')

    ctx = site_context()
    ctx.update({
        'projects': projects,
        'project': project,
        'unit': unit,
        'units': project.apartments.filter(is_active=True) if project else [],
        'today': timezone.now().date().isoformat(),
        'reference': request.GET.get('ref', ''),
        'slot_morning': ['10:00 AM', '11:00 AM', '12:00 PM'],
        'slot_noon': ['01:00 PM', '02:00 PM', '03:00 PM'],
        'slot_eve': ['04:00 PM', '05:00 PM', '06:00 PM'],
    })
    return render(request, 'website/booking.html', ctx)


@require_POST
def save_project(request):
    """Bookmark a project in the session (heart button on cards)."""
    slug = request.POST.get('slug')
    project = Project.objects.filter(slug=slug).first()
    if not project:
        return JsonResponse({'ok': False}, status=404)
    saved = request.session.get('saved_projects', [])
    key = str(project.pk)
    if key in saved:
        saved.remove(key)
        state = False
    else:
        saved.append(key)
        state = True
    request.session['saved_projects'] = saved
    return JsonResponse({'ok': True, 'saved': state, 'count': len(saved)})


def saved_projects(request):
    ids = request.session.get('saved_projects', [])
    ctx = site_context()
    ctx.update({
        'projects': project_queryset().filter(pk__in=ids),
        'ids': ids,
    })
    return render(request, 'website/saved.html', ctx)


def compare_projects(request):
    slugs = request.GET.getlist('p')[:4]
    projects = project_queryset().filter(slug__in=slugs)
    ctx = site_context()
    ctx.update({
        'projects': projects,
        'rows': _compare_rows(list(projects)),
        'all_projects': project_queryset()[:8],
    })
    return render(request, 'website/compare.html', ctx)


def _compare_rows(projects):
    if not projects:
        return []
    def row(label, fn):
        return {'label': label, 'values': [fn(p) for p in projects]}
    return [
        row('Stage', lambda p: p.stage_label),
        row('Location', lambda p: p.location.name),
        row('Starting price', lambda p: p.price_full),
        row('Per sq ft', lambda p: f'৳ {money(p.price_per_sqft)}' if p.price_per_sqft else '—'),
        row('Unit sizes', lambda p: p.size_range or '—'),
        row('Bedrooms', lambda p: p.bed_range or '—'),
        row('Land area', lambda p: f'{p.land_area} {p.land_area_unit}' if p.land_area else '—'),
        row('Floors', lambda p: p.floors or '—'),
        row('Total units', lambda p: p.total_units or '—'),
        row('Parking', lambda p: p.parking_spaces or '—'),
        row('Lifts', lambda p: p.lifts or '—'),
        row('Handover', lambda p: p.handover_date.strftime('%b %Y') if p.handover_date else '—'),
        row('Construction', lambda p: f'{p.completion_pct}%'),
        row('Ownership', lambda p: p.ownership_label),
        row('Amenities', lambda p: f'{p.amenities.count()} offered'),
    ]


# ---------------------------------------------------------------------------
# corporate pages
# ---------------------------------------------------------------------------
def about(request):
    ctx = site_context()
    ctx.update({
        'team': TeamMember.objects.filter(status=True),
        'leadership': TeamMember.objects.filter(status=True, is_leadership=True)[:4],
        'testimonials': Testimonial.objects.filter(status=True)[:4],
        'stats': insights_payload(),
        'posts': NewsPost.objects.filter(status=True)[:3],
        'gallery': GalleryImage.objects.filter(status=True)[:8],
    })
    return render(request, 'website/about.html', ctx)


def services(request):
    ctx = site_context()
    ctx.update({'services': Service.objects.filter(status=True)})
    return render(request, 'website/services.html', ctx)


def service_detail(request, slug):
    service = get_object_or_404(Service.objects.filter(status=True), slug=slug)
    ctx = site_context()
    ctx.update({
        'service': service,
        'others': Service.objects.filter(status=True).exclude(pk=service.pk)[:4],
    })
    return render(request, 'website/service_detail.html', ctx)


def news_list(request):
    kind = request.GET.get('kind', '')
    posts = NewsPost.objects.filter(status=True)
    if kind:
        posts = posts.filter(kind=kind)
    ctx = site_context()
    ctx.update({
        'posts': posts,
        'featured': posts.first(),
        'kinds': NewsPost.KIND,
        'active_kind': kind,
    })
    return render(request, 'website/news.html', ctx)


def news_detail(request, slug):
    post = get_object_or_404(NewsPost.objects.filter(status=True), slug=slug)
    ctx = site_context()
    ctx.update({
        'post': post,
        'others': NewsPost.objects.filter(status=True).exclude(pk=post.pk)[:3],
    })
    return render(request, 'website/news_detail.html', ctx)


def gallery(request):
    group = request.GET.get('group', '')
    images = GalleryImage.objects.filter(status=True)
    if group:
        images = images.filter(group=group)
    ctx = site_context()
    ctx.update({
        'images': images,
        'groups': GalleryImage.GROUP,
        'active_group': group,
        'total': images.count(),
    })
    return render(request, 'website/gallery.html', ctx)


def contact(request):
    if request.method == 'POST':
        project_id = request.POST.get('project')
        try:
            project_id = project_id if project_id and Project.objects.filter(pk=project_id).exists() else None
        except (TypeError, ValueError):
            project_id = None
        Enquiry.objects.create(
            name=request.POST.get('name', '').strip() or 'Guest',
            phone=request.POST.get('phone', '').strip(),
            email=request.POST.get('email', '').strip(),
            subject=request.POST.get('subject', 'buy'),
            project_id=project_id,
            message=request.POST.get('message', ''),
        )
        messages.success(request, 'Thank you for reaching out. Our team will respond shortly.')
        return redirect('/contact/?sent=1')
    ctx = site_context()
    ctx.update({
        'projects': Project.objects.live(),
        'faqs': Faq.objects.filter(status=True)[:6],
        'sent': request.GET.get('sent'),
    })
    return render(request, 'website/contact.html', ctx)


def faq(request):
    groups = {}
    for item in Faq.objects.filter(status=True):
        groups.setdefault(item.group, []).append(item)
    ctx = site_context()
    ctx.update({'groups': groups})
    return render(request, 'website/faq.html', ctx)


def land_sharing(request):
    projects = project_queryset().filter(Q(ownership='landshare') | Q(category='land'))
    ctx = site_context()
    ctx.update({
        'projects': projects,
        'stages': project_queryset().first().payment_stages.filter(status=True)
                  if project_queryset().first() else [],
        'faqs': Faq.objects.filter(status=True, group__icontains='land'),
        'locations': Location.objects.filter(status=True),
    })
    return render(request, 'website/land_sharing.html', ctx)


def investors(request):
    ctx = site_context()
    ctx.update({
        'projects': project_queryset()[:6],
        'locations': Location.objects.filter(status=True),
        'stats': insights_payload(),
        'testimonials': Testimonial.objects.filter(status=True)[:4],
    })
    return render(request, 'website/investors.html', ctx)


def search(request):
    q = request.GET.get('q', '').strip()
    projects = project_queryset()
    if q:
        projects = projects.filter(
            Q(name__icontains=q) | Q(location__name__icontains=q) |
            Q(address__icontains=q) | Q(tagline__icontains=q) |
            Q(description__icontains=q)).distinct()
    ctx = site_context()
    ctx.update({'q': q, 'projects': projects[:12], 'count': projects.count()})
    return render(request, 'website/search.html', ctx)


def page_not_found(request, exception=None):
    ctx = site_context()
    return render(request, 'website/404.html', ctx, status=404)


def robots_txt(request):
    """Simple robots file pointing at the sitemap."""
    from django.http import HttpResponse
    base = request.build_absolute_uri('/')
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        'Disallow: /cms/',
        'Disallow: /media/',
        '',
        f'Sitemap: {base}sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def set_prefs(request):
    """Persist language / theme choice in a cookie and return to the page."""
    from django.http import JsonResponse, HttpResponseRedirect
    from django.utils.http import url_has_allowed_host_and_scheme
    from .context_processors import LANG_COOKIE, THEME_COOKIE

    nxt = request.POST.get('next') or request.GET.get('next') or '/'
    if not url_has_allowed_host_and_scheme(nxt, allowed_hosts={request.get_host()},
                                           require_https=request.is_secure()):
        nxt = '/'

    lang = request.POST.get('lang') or request.GET.get('lang')
    theme = request.POST.get('theme') or request.GET.get('theme')

    if request.headers.get('x-requested-with') == 'fetch':
        if lang in ('en', 'bn'):
            return JsonResponse({'lang': lang})
        if theme in ('light', 'dark'):
            return JsonResponse({'theme': theme})
        return JsonResponse({'ok': False}, status=400)

    response = HttpResponseRedirect(nxt)
    # SameSite=None so the preference survives inside the cross-site preview
    # iframe; browsers require Secure alongside None, which is harmless on http
    # for a non-sensitive UI preference.
    for key, value, allowed in ((LANG_COOKIE, lang, ('en', 'bn')),
                                (THEME_COOKIE, theme, ('light', 'dark'))):
        if value in allowed:
            response.set_cookie(key, value, max_age=60 * 60 * 24 * 365,
                                samesite='None', secure=True, path='/')
    return response
