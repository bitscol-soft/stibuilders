from django.db import models
from ckeditor.fields import RichTextField
from realstateapp.models import UserRegistrations

# Create your models here.

class PhaseAdd(models.Model):
    phase_name       = models.CharField(max_length=200)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.phase_name

    class Meta:
        verbose_name = 'Phase'
        verbose_name_plural = 'Phase Add'



class LocationAdd(models.Model):
    location_name    = models.CharField(max_length=200)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location Add'


class ConstructionStatus(models.Model):
    construction_status      = models.CharField(max_length=300)
    status                   = models.BooleanField(default=True)

    def __str__(self):
        return self.construction_status

    class Meta:
        verbose_name = 'Construction'
        verbose_name_plural = 'Construction Status'


class Amenity(models.Model):
    amenity_name         = models.CharField(max_length=300)
    amenity_icon         = models.ImageField(upload_to='images/amenity_icon',blank=True)
    status               = models.BooleanField(default=True)

    def __str__(self):
        return self.amenity_name

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenity List'

class Facility(models.Model):
    facility_name         = models.CharField(max_length=300)
    facility_icon         = models.ImageField(upload_to='images/facility_icon',blank=True)
    status                = models.BooleanField(default=True)

    def __str__(self):
        return self.facility_name

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facility List'


class SalesStatus(models.Model):
    sales_status      = models.CharField(max_length=300)
    status            = models.BooleanField(default=True)

    def __str__(self):
        return self.sales_status

    class Meta:
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales Status'


class PropertyType(models.Model):
    property_type     = models.CharField(max_length=300)
    logo              = models.ImageField(upload_to='images/property_type_logo', blank=True)
    status            = models.BooleanField(default=True)

    def __str__(self):
        return self.property_type

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Type'



class ProjectAdd(models.Model):
    project_name      = models.CharField(max_length=300)
    project_logo      = models.ImageField(upload_to='project/logo',blank=True)
    developer_name    = models.CharField(max_length=200,blank=True,null=True)
    address           = models.CharField(max_length=200,blank=True,null=True)
    project_type      = models.ForeignKey(PropertyType, default=None, on_delete=models.CASCADE, blank = True, null=True)
    total_apartment   = models.IntegerField(default=0,blank=True,null=True)
    land_size         = models.CharField(max_length=300,blank=True,null=True)
    total_units       = models.IntegerField(default=0,blank=True,null=True)
    lift              = models.IntegerField(default=0,blank=True,null=True)
    stairs            = models.IntegerField(default=0,blank=True,null=True)
    face              = models.CharField(max_length=200,blank=True,null=True)
    plot_no           = models.CharField(max_length=200,blank=True,null=True)
    block_no          = models.CharField(max_length=200,blank=True,null=True)
    road_size         = models.CharField(max_length=200,blank=True,null=True)
    parking_ability   = models.CharField(max_length=200,blank=True,null=True)
    status            = models.BooleanField(default=True)
    created_by                   = models.ForeignKey(UserRegistrations,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Property Project List'

class ProjectPlotLand(models.Model):
    developer_name    = models.CharField(max_length=200,blank=True,null=True)
    block             = models.CharField(max_length=200,blank=True,null=True)
    sector            = models.IntegerField(default=0,blank=True,null=True)
    road_no           = models.IntegerField(default=0,blank=True,null=True)
    plot_no           = models.IntegerField(default=0,blank=True,null=True)
    land_size         = models.IntegerField(default=0,blank=True,null=True)
    size_unit         = models.CharField(max_length=200,blank=True, null=True)
    plot_land_image   = models.ImageField(upload_to='plot_land/plot_land_image',blank=True)
    address           = models.CharField(max_length=200,blank=True,null=True)
    map_url           = models.TextField(blank=True,null=True)
    status            = models.BooleanField(default=True)
    created_by        = models.ForeignKey(UserRegistrations,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.developer_name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Plot/Land Project List'


class PropertyEntry(models.Model):
    date                         = models.DateField(auto_now_add=False, blank=True, null=True)
    property_id                  = models.IntegerField(blank=True,null=True)
    label = (
        ('1', 'Upcoming'),
        ('2', 'Ongoing'),
        ('3', 'Completed'),
    )
    property_catagory            = models.CharField(max_length=2, choices=label)
    choose_phase                 = models.CharField(max_length=500,blank=True)
    property_type                = models.CharField(max_length=500,blank=True)
    location                     = models.CharField(max_length=500,blank=True)
    construction_status          = models.CharField(max_length=500,blank=True)
    project_name                 = models.CharField(max_length=500,blank=True)
    sales_type                   = models.CharField(max_length=500,blank=True)
    property_name                = models.CharField(max_length=1200,blank=True)
    selling_price                = models.CharField(max_length=1500,default=0)
    property_area                = models.CharField(max_length=500,blank=True)
    brochure                     = models.FileField(upload_to='property/brochure', blank=True,null=True)
    flor_plan                    = models.ImageField(upload_to='property/flor_plan', blank=True,null=True)
    bed                          = models.CharField(max_length=100,blank=True,null=True)
    bath                         = models.CharField(max_length=100,blank=True,null=True)
    number_of_belcony            = models.CharField(max_length=200,blank=True)
    daining_space                = models.CharField(max_length=200,blank=True)
    address                      = models.CharField(max_length=200,blank=True)
    flat_apartment_no            = models.CharField(max_length=200,blank=True)
    kitchen_space                = models.CharField(max_length=200,blank=True)
    property_image               = models.ImageField(upload_to='images/property_image', blank=True,null=True)
    property_banner              = models.ImageField(upload_to='images/property_banner', blank=True,null=True)
    location_map                 = models.TextField(blank=True)
    status                       = models.BooleanField(default=True)
    created_by                   = models.ForeignKey(UserRegistrations,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Entry'


class PropertyPhoto(models.Model):
    property_id                  = models.IntegerField(blank=True,null=True)
    property_photo               = models.ImageField(upload_to='images/property_photo',blank=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Photo'

class PropertyVideo(models.Model):
    property_id                  = models.IntegerField(blank=True,null=True)
    property_video_rul           = models.TextField(blank=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Video'

class PropertyOwnership(models.Model):
    property_id                  = models.IntegerField(blank=True,null=True)
    property_owner_name          = models.CharField(max_length=200,blank=True)
    property_ownership           = models.CharField(max_length=300,blank=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Ownership'


class PropertyAmenity(models.Model):
    property_id                  = models.IntegerField(blank=True,null=True)
    amenity_name                 = models.ForeignKey(Amenity,on_delete=models.CASCADE,blank=True,null=True)
    amenity_icon                 = models.ImageField(upload_to='amenity/amenity_icon',blank=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Amenity'


class PropertyFacility(models.Model):
    property_id                  = models.IntegerField(blank=True,null=True)
    facility_name                = models.ForeignKey(Facility,on_delete=models.CASCADE,blank=True,null=True)
    facility_icon                = models.ImageField(upload_to='fecility/facility_icon',blank=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.property_id)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property Facility'


class PlotLandStatus(models.Model):
    land_status_name                = models.CharField(max_length=200)
    status              = models.BooleanField(default=True)

    def __str__(self):
        return self.land_status_name

    class Meta:
        verbose_name = 'PlotLand'
        verbose_name_plural = 'Plot Land Status'

class MeasurementScale(models.Model):
    measurement_scale            = models.CharField(max_length=200)
    status                       = models.BooleanField(default=True)

    def __str__(self):
        return self.measurement_scale

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurement Scale'


class LandFacilityEntry(models.Model):
    land_facility_name         = models.CharField(max_length=300)
    status                = models.BooleanField(default=True)

    def __str__(self):
        return self.land_facility_name

    class Meta:
        verbose_name = 'PlotLand Facility'
        verbose_name_plural = 'PlotLand Facility Entry'

class PlotLandEntry(models.Model):
    date                         = models.DateField(auto_now_add=False, blank=True, null=True)
    plotland_id                  = models.IntegerField(blank=True,null=True)
    plot_land_image              = models.ImageField(upload_to='plot/plot_land_image',blank=True)
    plot_land_status             = models.ForeignKey(PlotLandStatus, default=None, on_delete=models.CASCADE, blank = True, null=True)
    land_size                    = models.IntegerField(blank=True,null=True)
    measurement_scale            = models.ForeignKey(MeasurementScale, default=None, on_delete=models.CASCADE, blank = True, null=True)
    developer_name               = models.ForeignKey(ProjectPlotLand, default=None, on_delete=models.CASCADE, blank = True, null=True)
    block                        = models.CharField(max_length=1200,blank=True)
    sector                       = models.IntegerField(blank=True,null=True)
    road_no                      = models.IntegerField(blank=True,null=True)
    plot_no                      = models.IntegerField(blank=True,null=True)
    google_map_url               = models.TextField(blank=True,null=True)
    address                      = models.TextField(blank=True,null=True)
    status                       = models.BooleanField(default=True)
    created_by                   = models.ForeignKey(UserRegistrations,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __int__(self):
        return int(self.plotland_id)

    class Meta:
        verbose_name = 'PlotLand'
        verbose_name_plural = 'Plot / Land Entry'





class PlotLandFacility(models.Model):
    plotland_id                  = models.IntegerField(blank=True,null=True)
    land_facility                = models.ForeignKey(LandFacilityEntry,on_delete=models.CASCADE,blank=True,null=True)
    status                       = models.BooleanField(default=True)

    def __int__(self):
        return int(self.plotland_id)

    class Meta:
        verbose_name = 'PlotLand'
        verbose_name_plural = 'PlotLand Facility'


