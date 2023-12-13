from distutils.command.upload import upload
from pyexpat import model
from tokenize import blank_re
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class CompanyProfile(models.Model):
    company_name    = models.CharField(max_length=100)
    logo          	= models.ImageField(upload_to='images/logo', blank=True)
    slugan       	= models.CharField(max_length=100, blank=True,null=True)
    email        	= models.EmailField(max_length=100, blank=True,null=True)
    mobile      	= models.CharField(max_length=15, blank=True,null=True)
    mobile1      	= models.CharField(max_length=15, blank=True,null=True)
    phone1      	= models.CharField(max_length=15, blank=True,null=True)
    address      	= models.TextField(blank=True,null=True)
    about           = RichTextField(blank=True,null=True)
    staring_year  	= models.IntegerField(default = 0)
    google_map_link = models.TextField(blank=True,null=True)
    copy_right    	= models.CharField(max_length=50, blank=True,null=True)
    facebook_link   = models.CharField(max_length=200, blank=True,null=True)
    twitter_link    = models.CharField(max_length=200, blank=True,null=True)
    linkedin_link   = models.CharField(max_length=200, blank=True,null=True)
    youtube_link    = models.CharField(max_length=200, blank=True,null=True)
    whatsapp_link   = models.CharField(max_length=200, blank=True,null=True)
    instragram_link = models.CharField(max_length=200, blank=True,null=True)
    status       	= models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company Profile'


class SliderBanner(models.Model):
    title          = models.TextField(blank=True)
    slider_banner  = models.ImageField(upload_to='images/slider_banner',blank=True)
    short_description  = models.TextField(blank=True)
    button_text        = models.CharField(max_length=100,blank=True)
    button_url  = models.CharField(max_length=200,blank=True)
    slider_order   = models.IntegerField()
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider Banner List'



class UserRegistrations(models.Model):
    label = (
        ('1', 'Admin'),
        ('2', 'Editor'),
    )
    user_type     = models.CharField(max_length=2, choices=label,blank=True,null=True)
    full_name     = models.CharField(max_length=256)
    user_mobile   = models.CharField(max_length=256)
    email         = models.CharField(max_length=256,blank=True)
    photo         = models.ImageField(upload_to='images/user_photo',blank=True)
    user_password = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    address       = models.TextField(blank=True)
    status        = models.BooleanField(default=1)
     
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User List'


class ServiceEntry(models.Model):
    service_name    = models.CharField(max_length=200)
    status          = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'Service Entry'


class ServiceDetails(models.Model):
    service_name          = models.ForeignKey(ServiceEntry, default=None, on_delete=models.CASCADE, blank = True, null=True)
    service_banner        = models.ImageField(upload_to='images/service_banner', blank=True)
    service_title         = models.CharField(max_length=300,blank=True)
    service_image         = models.ImageField(upload_to='images/service_image', blank=True)
    service_description   = RichTextField(blank=True)
    status                = models.BooleanField(default=True)

    def __str__(self):
        return self.service_title

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'Service Details'


class SisternConcernEntry(models.Model):
    sister_concern_name    = models.CharField(max_length=200)
    status                 = models.BooleanField(default=True)

    def __str__(self):
        return self.sister_concern_name

    class Meta:
        verbose_name = 'sister  concern'
        verbose_name_plural = 'Sister  Concern Entry'



class SisternConcernDetails(models.Model):
    sister_concern_name          = models.ForeignKey(SisternConcernEntry, default=None, on_delete=models.CASCADE, blank = True, null=True)
    sister_concern_banner        = models.ImageField(upload_to='images/sister_concern_banner', blank=True)
    sister_concern_image         = models.ImageField(upload_to='images/sister_concern_image', blank=True)
    address                      = models.CharField(max_length=1000,blank=True)
    mobile                       = models.CharField(max_length=14,blank=True)
    email                        = models.EmailField(blank=True)
    facebook_link                = models.CharField(max_length=1200, blank=True)
    twitter_link                 = models.CharField(max_length=1200, blank=True)
    linkedin_link                = models.CharField(max_length=1200, blank=True)
    youtube_link                 = models.CharField(max_length=1200, blank=True)
    service_description          = RichTextField(blank=True)
    status                       = models.BooleanField(default=True)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name = 'Sistern Concern'
        verbose_name_plural = 'Sistern Concern Details'








class TeamMemberInfo(models.Model):
    member_name           = models.CharField(max_length=200,blank=True)
    member_image          = models.ImageField(upload_to='images/Team_member', blank=True)
    member_disignation    = models.CharField(max_length=300,blank=True)
    facebook_link         = models.CharField(max_length=200, blank=True)
    twitter_link          = models.CharField(max_length=200, blank=True)
    instragram_link       = models.CharField(max_length=200, blank=True)
    member_order          = models.IntegerField()
    status                = models.BooleanField(default=True)
    def __str__(self):
        return self.member_name
    
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Member Entry'



class EventGallery(models.Model):
    picture      = models.ImageField(upload_to='images/event_gallery', blank=True)
    status       = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Event Gallery'
        verbose_name_plural = 'Event Gallery List'

class AffiliateSupplierAdd(models.Model):
    name         = models.CharField(max_length=500, blank=True)
    logo         = models.ImageField(upload_to='images/affiliate_supplier', blank=True)
    status       = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Affiliate Supplier'
        verbose_name_plural = 'Affiliate & Supplier Add'

class ChairMessage(models.Model):
    name            = models.CharField(max_length=500, blank=True)
    designation     = models.CharField(max_length=500, blank=True)
    image           = models.ImageField(upload_to='images/message_image', blank=True)
    message         = models.TextField(blank=True)
    facebook_link   = models.CharField(max_length=200, blank=True)
    twitter_link    = models.CharField(max_length=200, blank=True)
    instragram_link = models.CharField(max_length=200, blank=True)
    status          = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Message Add'


class QualityAdd(models.Model):
    quality_title    = models.CharField(max_length=500, blank=True)
    quality_text     = models.TextField(blank=True)
    image            = models.ImageField(upload_to='images/quality_image', blank=True)
    status           = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Quality'
        verbose_name_plural = 'Quality Add'


class CertifiedAdd(models.Model):
    certified_title  = models.CharField(max_length=500, blank=True)
    certified_text   = models.TextField(blank=True)
    status           = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Certified'
        verbose_name_plural = 'Certified Add'


class TestimonialAdd(models.Model):
    name         = models.CharField(max_length=500, blank=True,null=True)
    profession   = models.CharField(max_length=500, blank=True,null=True)
    image            = models.ImageField(upload_to='images/testimonial_image', blank=True)
    testimonial  = models.TextField(blank=True,null=True)
    status       = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Client Testimonial'

class TestimonialVideo(models.Model):
    name                         = models.CharField(max_length=500, blank=True)
    testimonial_video_url_link   = models.CharField(max_length=1500, blank=True)
    status       = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Client Testimonial Video'

class HotNumber(models.Model):
    title           = models.CharField(max_length=500, blank=True)
    number          = models.CharField(max_length=15, blank=True)
    status          = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'HotNumber'
        verbose_name_plural = 'Hot Number Add'




class ContactMessage(models.Model):
    name                 = models.CharField(max_length=500, blank=True)
    email                = models.EmailField(blank=True)
    property_plot_type   = models.CharField(max_length=1500, blank=True)
    location             = models.CharField(max_length=1500, blank=True)
    apartment_size       = models.CharField(max_length=1500, blank=True)
    message              = models.TextField(blank=True)
    status               = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Message List'

class TermsConditions(models.Model):
    title                = models.CharField(max_length=500, blank=True)
    picture              = models.ImageField(upload_to='images/testimonial_image', blank=True)
    terms_conditions     = RichTextField(blank=True)
    status               = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Terms'
        verbose_name_plural = 'Terms Conditions'




class PrivacyPolicy(models.Model):
    title                = models.CharField(max_length=500, blank=True)
    picture              = models.ImageField(upload_to='images/testimonial_image', blank=True)
    privacy_policy       = RichTextField(blank=True)
    status               = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Privacy'
        verbose_name_plural = 'Privacy Policy'
        
        
class Faq(models.Model):
    question             = models.CharField(max_length=800, blank=True)
    answer               = models.TextField(blank=True)
    status               = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.question)
    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faq Entry'        
        
        
        