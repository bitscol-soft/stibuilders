from django.contrib import admin

from .models import *

# Register your models here.
class PhaseAddAdmin(admin.ModelAdmin):
    list_display   = ('phase_name', 'status')
    list_filter    = ('phase_name', 'status')


class LocationAddAdmin(admin.ModelAdmin):
    list_display   = ('location_name', 'status')
    list_filter    = ('location_name', 'status')

    
class ProjectAddAdmin(admin.ModelAdmin):
    list_display   = ('project_name', 'developer_name', 'status')
    list_filter    = ('project_name', 'developer_name', 'status')

class ProjectPlotLandAdmin(admin.ModelAdmin):
    list_display   = ('developer_name', 'block', 'address', 'status')
    list_filter    = ('developer_name', 'block', 'status')


class PropertyEntryAdmin(admin.ModelAdmin):
    list_display   = ('property_name', 'property_catagory', 'status')
    list_filter    = ('property_name', 'property_catagory', 'status')

class PlotLandEntryAdmin(admin.ModelAdmin):
    list_display   = ('plotland_id', 'developer_name','block', 'status')
    list_filter    = ('plotland_id', 'developer_name','block', 'status')



admin.site.register(PhaseAdd,PhaseAddAdmin)
admin.site.register(LocationAdd,LocationAddAdmin)
admin.site.register(ProjectAdd,ProjectAddAdmin)
admin.site.register(ProjectPlotLand,ProjectPlotLandAdmin)
admin.site.register(PropertyEntry,PropertyEntryAdmin)
admin.site.register(ConstructionStatus)
admin.site.register(Amenity)
admin.site.register(Facility)
admin.site.register(SalesStatus)
admin.site.register(PropertyType)
admin.site.register(PropertyPhoto)
admin.site.register(PropertyVideo)
admin.site.register(PropertyAmenity)
admin.site.register(PropertyFacility)
admin.site.register(PropertyOwnership)
admin.site.register(PlotLandStatus)
admin.site.register(MeasurementScale)
admin.site.register(LandFacilityEntry)
admin.site.register(PlotLandEntry,PlotLandEntryAdmin)
admin.site.register(PlotLandFacility)
