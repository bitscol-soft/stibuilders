import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models import (Amenity, Apartment, Booking, Enquiry, Faq, Feature, GalleryImage,
                     Landmark, Location, Milestone, NewsPost, PaymentStage, Project,
                     ProjectFloorPlan, ProjectImage, Service, SiteSetting, TeamMember,
                     Testimonial)

admin.site.site_header = 'STI Builders — Control Panel'
admin.site.site_title = 'STI Builders Admin'
admin.site.index_title = 'Website & Project Management'


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'category', 'order', 'status')


class FloorPlanInline(admin.TabularInline):
    model = ProjectFloorPlan
    extra = 1
    fields = ('title', 'kind', 'image', 'area_sft', 'beds', 'baths', 'order', 'status')


class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1
    fields = ('title', 'target_date', 'completed_date', 'progress_pct', 'is_done', 'order')


class PaymentStageInline(admin.TabularInline):
    model = PaymentStage
    extra = 1
    fields = ('title', 'share_pct', 'timing', 'note', 'order')


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1
    fields = ('unit_no', 'unit_type', 'title', 'size_sft', 'beds', 'baths', 'price', 'status')


class LandmarkInline(admin.TabularInline):
    model = Landmark
    extra = 1
    fields = ('name', 'category', 'distance_km', 'drive_minutes', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage', 'category', 'location', 'price_from', 'completion_pct',
                    'featured', 'published', 'thumb')
    list_filter = ('stage', 'category', 'ownership', 'location', 'featured', 'published')
    search_fields = ('name', 'code', 'address', 'location__name')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('amenities', 'features')
    inlines = [ApartmentInline, ProjectImageInline, FloorPlanInline, MilestoneInline,
               PaymentStageInline]
    list_editable = ('featured', 'published')
    save_on_top = True
    fieldsets = (
        ('Identity', {'fields': ('name', 'slug', 'code', 'tagline', 'category', 'stage',
                                 'ownership', 'featured', 'published', 'status', 'order')}),
        ('Location', {'fields': ('location', 'address', 'map_embed_url', 'map_latitude',
                                 'map_longitude')}),
        ('Story', {'fields': ('short_description', 'description', 'concept_note')}),
        ('Media', {'fields': ('cover_image', 'night_image', 'logo', 'hero_video_url',
                              'brochure', 'brochure_note')}),
        ('Building information', {'classes': ('collapse',), 'fields': (
            'land_area', 'land_area_unit', 'floors', 'basement_levels', 'total_units',
            'units_per_floor', 'lifts', 'staircases', 'parking_spaces', 'facing', 'road_width',
            'plot_no', 'block_no', 'architect', 'structural_consultant', 'rajuk_number',
            'approval_authority')}),
        ('Pricing & availability', {'classes': ('collapse',), 'fields': (
            'price_from', 'price_per_sqft', 'size_from', 'size_to', 'beds_from', 'beds_to',
            'booking_amount')}),
        ('Timeline', {'classes': ('collapse',), 'fields': (
            'launch_date', 'handover_date', 'completion_pct')}),
        ('Amenities & features', {'classes': ('collapse',), 'fields': ('amenities', 'features')}),
        ('Videos', {'classes': ('collapse',), 'fields': ('video_1_url', 'video_2_url',
                                                         'video_3_url')}),
        ('Social sharing', {'classes': ('collapse',), 'fields': (
            'facebook_url', 'instagram_url', 'youtube_url', 'linkedin_url', 'social_hashtag')}),
        ('Land sharing breakdown', {'classes': ('collapse',), 'fields': (
            'land_owner_share', 'developer_share', 'land_share_note')}),
    )

    @admin.display(description='')
    def thumb(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height:38px;border-radius:6px">',
                               obj.cover_image.url)
        return '—'


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('project', 'label', 'unit_type', 'size_sft', 'beds', 'baths', 'price',
                    'status')
    list_filter = ('project', 'status', 'unit_type')
    search_fields = ('project__name', 'title', 'unit_no')
    filter_horizontal = ('features',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone', 'project_total', 'avg_price_per_sqft', 'price_growth_yoy',
                    'demand_index', 'livability_score', 'status')
    list_filter = ('zone', 'status', 'city')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'zone')
    inlines = [LandmarkInline]
    fieldsets = (
        ('Basics', {'fields': ('name', 'slug', 'city', 'zone', 'short_note', 'description',
                               'cover_image', 'order', 'status')}),
        ('Map', {'fields': ('latitude', 'longitude')}),
        ('Analytics', {'fields': ('avg_price_per_sqft', 'price_growth_yoy', 'rental_yield',
                                  'demand_index', 'livability_score', 'commute_minutes',
                                  'schools_count', 'hospitals_count', 'malls_count',
                                  'green_space_pct')}),
        ('Highlights', {'fields': ('highlight_1', 'highlight_2', 'highlight_3', 'road_access')}),
    )

    @admin.display(description='Projects')
    def project_total(self, obj):
        return obj.projects.filter(status=True, published=True).count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order', 'status')
    list_editable = ('order', 'status')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'status')
    list_editable = ('order', 'status')


def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    fields = [f.name for f in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta.model_name}.csv'
    writer = csv.writer(response)
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, f) for f in fields])
    return response


export_as_csv.short_description = 'Export selected rows as CSV'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_display = ('reference', 'full_name', 'phone', 'project', 'kind', 'preferred_date',
                    'status', 'created_at')
    list_filter = ('status', 'kind', 'project')
    search_fields = ('reference', 'full_name', 'phone', 'email')
    readonly_fields = ('reference', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_display = ('name', 'phone', 'subject', 'project', 'is_read', 'created_at')
    list_filter = ('subject', 'is_read')
    search_fields = ('name', 'phone', 'email', 'message')


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'category', 'order', 'status')
    list_filter = ('project', 'category')


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'target_date', 'progress_pct', 'is_done')
    list_filter = ('project', 'is_done')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order', 'status')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_leadership', 'order', 'status')
    list_editable = ('order', 'status')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'project', 'rating', 'status')
    list_filter = ('status', 'rating')


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'published_at', 'read_minutes', 'status')
    list_filter = ('kind', 'status')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'group', 'order', 'status')
    list_filter = ('group', 'status')
    list_editable = ('order', 'status')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'group', 'project', 'order', 'status')
    list_filter = ('group', 'status')


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return SiteSetting.objects.count() < 1


admin.site.register(ProjectFloorPlan)
admin.site.register(PaymentStage)
admin.site.register(Landmark)
