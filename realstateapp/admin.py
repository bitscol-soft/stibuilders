from django.contrib import admin

from .models import *
# Register your models here.
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display   = ('company_name', 'email', 'mobile', 'address', 'status')
    list_filter    = ('company_name', 'email', 'mobile', 'status')
    search_fields  = ('company_name', 'email','mobile')



class SliderBannerAdmin(admin.ModelAdmin):
    list_display   = ('title', 'slider_banner', 'slider_order', 'status')
    list_filter    = ('title', 'slider_banner', 'slider_order', 'status')

class UserRegistrationsAdmin(admin.ModelAdmin):
    list_display   = ('full_name','user_type', 'user_mobile', 'status')
    list_filter    = ('full_name', 'user_mobile', 'status')


class ChairMessageAdmin(admin.ModelAdmin):
    list_display   = ('name', 'designation', 'status')
    list_filter    = ('name', 'designation', 'status')

admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(SliderBanner, SliderBannerAdmin)
admin.site.register(UserRegistrations, UserRegistrationsAdmin)
admin.site.register(ChairMessage, ChairMessageAdmin)
admin.site.register(TeamMemberInfo)
admin.site.register(EventGallery)
admin.site.register(QualityAdd)
admin.site.register(TestimonialAdd)
admin.site.register(HotNumber)
admin.site.register(TermsConditions)
admin.site.register(PrivacyPolicy)
admin.site.register(ServiceEntry)
admin.site.register(ServiceDetails)
admin.site.register(SisternConcernEntry)
admin.site.register(SisternConcernDetails)
