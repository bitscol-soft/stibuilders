from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse, Http404
from numpy import choose
from realstateapp.models import * 
from property.models import * 
from django.contrib import messages
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import datetime
def home(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_mess        = ChairMessage.objects.filter(status=1).first()
    get_team        = TeamMemberInfo.objects.filter(status=1).order_by('member_order')
    hot_number      = HotNumber.objects.filter(status=1)
    get_testi       = TestimonialAdd.objects.filter(status=1)
    getservice      = ServiceDetails.objects.filter(status=1)
    concern_entry   = SisternConcernDetails.objects.filter(status=1)
    context={  
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_mess':get_mess,
        'get_team':get_team,
        'hot_number':hot_number,
        'get_testi':get_testi,
        'getservice':getservice,
        'concern_entry':concern_entry,
    }
    return render(request,'realstateapp/website/index.html',context)


def property_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    ser_entry       = ServiceEntry.objects.all()
    concern_entry   = SisternConcernEntry.objects.all()
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_up          = PropertyEntry.objects.filter(property_catagory=1,status=1)
    get_on          = PropertyEntry.objects.filter(property_catagory=2,status=1)
    get_com         = PropertyEntry.objects.filter(property_catagory=3,status=1)
    hot_number      = HotNumber.objects.filter(status=1)
    testimonial     = TestimonialAdd.objects.filter(status=1)


   

    context ={
        'get_profile':comprofile,
        'ser_entry':ser_entry,
        'concern_entry':concern_entry,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_up':get_up,
        'get_on':get_on,
        'get_com':get_com,
        'hot_number':hot_number,
        'client_testi':testimonial,
    }

    return render(request,'realstateapp/website/property/all-property-list.html',context)



def property_search(request):
    comprofile      = CompanyProfile.objects.all().first()
    ser_entry       = ServiceEntry.objects.all()
    concern_entry   = SisternConcernEntry.objects.all()
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_up          = PropertyEntry.objects.filter(property_catagory=1,status=1)
    get_on          = PropertyEntry.objects.filter(property_catagory=2,status=1)
    get_com         = PropertyEntry.objects.filter(property_catagory=3,status=1)
    aminity         = Amenity.objects.filter(status=1)
    hot_number      = HotNumber.objects.filter(status=1)
    testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method == "POST":
        phase_name       = request.POST.get('phase_name')
        property_type       = request.POST.get('property_type')
        location_name       = request.POST.get('location_name')
        min_price           = request.POST.get('min_price')
        max_price           = request.POST.get('max_price')
        min_area            = request.POST.get('min_area')
        max_area            = request.POST.get('max_area')
        bed                 = request.POST.get('bed')
        bath                = request.POST.get('bath')

        arr = []
        query_str = ""
        get_result = ""

        if phase_name:
            arr.append(phase_name)
            query_str += " and choose_phase = %s"
            
        if property_type:
            arr.append(property_type)
            query_str += " and property_type = %s"
            
        if location_name:
            arr.append(location_name)
            query_str += " and location = %s"
     
        
    
        if min_price:
            print("Test 1")
            arr.append(str(min_price))
            query_str += " and selling_price >= %s"

        if max_price:
            print("Test 2")
            arr.append(str(max_price))
            query_str += " and selling_price <= %s"
        
        if min_area:
            print("Test 3")
            arr.append(str(min_area))
            query_str += " and area >= %s"

        if max_area:
            print("Test 4")
            arr.append(str(max_area))
            query_str += " and area <= %s"
        
        if bed:
            arr.append(bed)
            query_str += " and bed = %s" 
        
        if bath:
            arr.append(bath)
            query_str += " and bath = %s" 

        # if min_price and max_price:
        #     print("Test 2 price") 
        #     query_str += " and price >= "+str(min_price)+" and price <= "+str(max_price)
 
        print("query_str: ", query_str)
        get_result = PropertyEntry.objects.raw("SELECT * FROM `property_propertyentry` WHERE status = 1"+query_str+" order by id asc ", arr)
        print("get_result:", get_result.query)

        context = {
            'get_result':get_result,
            'get_profile':comprofile,
            'ser_entry':ser_entry,
            'concern_entry':concern_entry,
            'get_phase':phase,
            'add_property':add_property,
            'get':get_location,
            'get_up':get_up,
            'get_on':get_on,
            'get_com':get_com,
            'aminity':aminity,
            'hot_number':hot_number,
            'client_testi':testimonial,
        }
        return render(request,'realstateapp/website/property/property-search.html', context)
       
    else:
        context ={
            'get_profile':comprofile,
            'ser_entry':ser_entry,
            'concern_entry':concern_entry,
            'get_phase':phase,
            'add_property':add_property,
            'get':get_location,
            'get_up':get_up,
            'get_on':get_on,
            'get_com':get_com,
            'aminity':aminity,
            'hot_number':hot_number,
            'client_testi':testimonial,
        }

        return render(request,'realstateapp/website/property/property-search.html',context)

def property_details(request,property_id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)

    get_property    = PropertyEntry.objects.get(property_id=property_id)
    get_image       = PropertyPhoto.objects.filter(property_id=property_id)
    get_video       = PropertyVideo.objects.filter(property_id=property_id)
    get_amenity     = PropertyAmenity.objects.filter(property_id=property_id)
    get_facility    = PropertyFacility.objects.filter(property_id=property_id)
    get_owner       = PropertyOwnership.objects.filter(property_id=property_id)

    getid           = get_property.project_name
    get_project     = ProjectAdd.objects.get(project_name=getid)
    print("obj", get_project)
    concern_entry   = SisternConcernDetails.objects.filter(status=1)

    context={  
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
    

        'get_property':get_property,
        'get_image':get_image,
        'get_video':get_video,
        'get_project':get_project,
        'get_amenity':get_amenity,
        'get_facility':get_facility,
        'get_owner':get_owner,
        'concern_entry':concern_entry,
    }
    return render(request,'property/dashboard/property-detail.html',context)




def search_all_property(request):
    comprofile      = CompanyProfile.objects.all().first()
    ser_entry       = ServiceEntry.objects.all()
    concern_entry   = SisternConcernEntry.objects.all()
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_up          = PropertyEntry.objects.filter(property_catagory=1,status=1)
    get_on          = PropertyEntry.objects.filter(property_catagory=2,status=1)
    get_com         = PropertyEntry.objects.filter(property_catagory=3,status=1)
    hot_number      = HotNumber.objects.filter(status=1)
    testimonial     = TestimonialAdd.objects.filter(status=1)
    
    if request.method == "POST":
        phase_name          = request.POST.get('phase_name')
        property_type       = request.POST.get('property_type')
        location_name       = request.POST.get('location_name')
        min_price           = request.POST.get('min_price')
        max_price           = request.POST.get('max_price')
        min_area            = request.POST.get('min_area')
        max_area            = request.POST.get('max_area')
        bed                 = request.POST.get('bed')
        bath                = request.POST.get('bath')

        arr = []
        query_str = ""
        get_result = ""

        if phase_name:
            arr.append(phase_name)
            query_str += " and choose_phase = %s"
            
        if property_type:
            arr.append(property_type)
            query_str += " and property_type = %s"
            
        if location_name:
            arr.append(location_name)
            query_str += " and location = %s"

        
    
        if min_price:
            print("Test 1")
            arr.append(str(min_price))
            query_str += " and selling_price >= %s"

        if max_price:
            print("Test 2")
            arr.append(str(max_price))
            query_str += " and selling_price <= %s"
        
        if min_area:
            print("Test 3")
            arr.append(str(min_area))
            query_str += " and property_area >= %s"

        if max_area:
            print("Test 4")
            arr.append(str(max_area))
            query_str += " and property_area <= %s"
        
        if bed:
            arr.append(bed)
            query_str += " and bed = %s" 
        
        if bath:
            arr.append(bath)
            query_str += " and bath = %s" 

        # if min_price and max_price:
        #     print("Test 2 price") 
        #     query_str += " and price >= "+str(min_price)+" and price <= "+str(max_price)
 
        print("query_str: ", query_str)
        get_result = PropertyEntry.objects.raw("SELECT * FROM `property_propertyentry` WHERE status = 1"+query_str+" order by id asc ", arr)
        print("get_result:", get_result.query)

        context = {
            'get_result':get_result,
            'get_profile':comprofile,
            'ser_entry':ser_entry,
            'concern_entry':concern_entry,
            'get_phase':phase,
            'add_property':add_property,
            'get':get_location,
            'get_up':get_up,
            'get_on':get_on,
            'get_com':get_com,
            'hot_number':hot_number,
            'client_testi':testimonial,
        }
        return render(request,'realstateapp/website/property/search-all-property.html', context)

   
    else:
        context ={
            'get_profile':comprofile,
            'ser_entry':ser_entry,
            'concern_entry':concern_entry,
            'get_phase':phase,
            'add_property':add_property,
            'get':get_location,
            'get_up':get_up,
            'get_on':get_on,
            'get_com':get_com,
            'hot_number':hot_number,
            'client_testi':testimonial,
        }

    return render(request,'realstateapp/website/property/search-all-property.html',context)


def phase_wise_property(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    getphase        = PhaseAdd.objects.get(id=id)
    property        = PropertyEntry.objects.filter(choose_phase=getphase)
    concern_entry   = SisternConcernDetails.objects.filter(status=1)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'getphase':getphase,
        'get_property':property,
        'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/property/phase-wise-property.html',context)


def type_wise_property_list(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get             = PropertyType.objects.get(id=id)
    property        = PropertyEntry.objects.filter(property_type=get)
    concern_entry   = SisternConcernDetails.objects.filter(status=1)

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_type':get,
        'get_property':property,
        'concern_entry':concern_entry,
    }
    return render(request,'realstateapp/website/property/type-wise-property-list.html',context)

def location_wise_property_list(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_locat       = LocationAdd.objects.get(id=id)
    property        = PropertyEntry.objects.filter(location=get_locat)
    concern_entry   = SisternConcernDetails.objects.filter(status=1)

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_locat':get_locat,
        'get_property':property,
        'concern_entry':concern_entry,
    }
    return render(request,'realstateapp/website/property/location-wise-property-list.html',context)


def dash_login(request):
    comprofile      = CompanyProfile.objects.all().first()
    if request.method=="POST":
        user_mobile=request.POST['user_mobile']
        user_password=request.POST['user_password']
        data = UserRegistrations.objects.filter(user_mobile=user_mobile, user_password=user_password,status=1).first()
        
        if data:
            request.session['user_mobile'] = data.user_mobile
            request.session['password'] = data.user_password
            request.session['userid'] = data.id 
    
            return redirect('/dashboard-page/')
        else:
            messages.info(request, 'something went wrong!')
            return render(request,'realstateapp/dashboard/dashboard-login.html')
    
    context={
        'get_profile':comprofile,
    }

    return render(request,'realstateapp/dashboard/dashboard-login.html',context)


def dashboard_page(request):
    user            = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    get_property    = PropertyEntry.objects.all().count()
    get_plot        = PlotLandEntry.objects.all().count()
    get_up          = PropertyEntry.objects.filter(property_catagory=1).count()
    get_on          = PropertyEntry.objects.filter(property_catagory=2).count()
    get_com         = PropertyEntry.objects.filter(property_catagory=3).count()
    get_project     = ProjectAdd.objects.all().count()
    getplot         = ProjectPlotLand.objects.all().count()

    get_total       = int(get_project + getplot)
    
    context={
        'user':user,
        'get_profile':comprofile,
        'get_property':get_property,
        'get_plot':get_plot,
        'get_up':get_up,
        'get_on':get_on,
        'get_com':get_com,
        'get_total':get_total,
    }
    return render(request,'realstateapp/dashboard/dashboard.html',context)


def logout(request):
    request.session['userid'] = False
    return redirect('/dashboard-login/')

def auth_register(request):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()

    if request.method=="POST":
        full_name  = request.POST.get('full_name')
        user_mobile  = request.POST.get('user_mobile')
        user_type      = request.POST.get('user_type')
        user_password  = request.POST.get('user_password')
        email  = request.POST.get('email')
        address  = request.POST.get('address')

        document_path = ""
        if bool(request.FILES.get('photo', False)) == True:
            file = request.FILES['photo']   
            if not os.path.exists("user_images/"):
                os.mkdir("user_images/")

            document_path = default_storage.save("user_images/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("user_images/")+str(document_path).split("/")[-1] 

        UserRegistrations.objects.create(full_name=full_name,user_mobile=user_mobile,user_type=user_type,user_password=user_password,
        email=email,photo=document_path,address=address)
        messages.success(request,'User has been created successfully.')
        return redirect('/auth-register/')
    
    context={
        'user':user,
        'get_profile':comprofile,
    }

    return render(request,'realstateapp/dashboard/auth-register.html',context)


def auth_list(request):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    alluser = UserRegistrations.objects.all()

 
    context={
        'user':user,
        'get_profile':comprofile,
        'alluser':alluser,

    }

    return render(request,'realstateapp/dashboard/auth-list.html',context)


def auth_edit(request,id):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getuser = UserRegistrations.objects.get(id=id)

    if request.method=="POST":
        full_name  = request.POST.get('full_name')
        user_mobile  = request.POST.get('user_mobile')
        user_type      = request.POST.get('user_type')
        user_password  = request.POST.get('user_password')
        email  = request.POST.get('email')
        address  = request.POST.get('address')

        photo = str(getuser.photo) if getuser.photo else ""
        if bool(request.FILES.get('photo', False)) == True: 
            if os.path.exists(str(photo)):
                os.remove(str(getuser.photo))

            file = request.FILES['photo']
            photo = "photo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/photo/'):
                os.mkdir('realstateapp/static/realstateapp/media/photo/') 
            photo = default_storage.save("photo/"+file.name, ContentFile(file.read())) 
            if photo:
                photo = str("photo/")+str(photo).split("/")[-1]

        UserRegistrations.objects.filter(id=id).update(full_name=full_name,user_mobile=user_mobile,
        user_type=user_type,user_password=user_password,
        email=email,photo=photo,address=address)
        messages.success(request,'User has been updated successfully.')
        return redirect('/auth-list/')
    
    context={
        'user':user,
        'get_profile':comprofile,
        'getuser':getuser,
    }

    return render(request,'realstateapp/dashboard/auth-edit.html',context)


def auth_edit_user(request,id):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getuser = UserRegistrations.objects.get(id=id)

    if request.method=="POST":
        full_name      = request.POST.get('full_name')
        user_mobile    = request.POST.get('user_mobile')
        user_password  = request.POST.get('user_password')
        email  = request.POST.get('email')
        address  = request.POST.get('address')

        photo = str(getuser.photo) if getuser.photo else ""
        if bool(request.FILES.get('photo', False)) == True: 
            if os.path.exists(str(photo)):
                os.remove(str(getuser.photo))

            file = request.FILES['photo']
            photo = "photo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/photo/'):
                os.mkdir('realstateapp/static/realstateapp/media/photo/') 
            photo = default_storage.save("photo/"+file.name, ContentFile(file.read())) 
            if photo:
                photo = str("photo/")+str(photo).split("/")[-1]

        UserRegistrations.objects.filter(id=id).update(full_name=full_name,user_mobile=user_mobile,
            user_password=user_password,
            email=email,photo=photo,address=address)
        messages.success(request,'User has been updated successfully.')
        return redirect('/auth-profile/')
    
    context={
        'user':user,
        'get_profile':comprofile,
        'getuser':getuser,
    }

    return render(request,'realstateapp/dashboard/auth-edit-user.html',context)


def auth_profile(request):
    user            = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    
    context={
        'user':user,
        'get_profile':comprofile,
    }

    return render(request,'realstateapp/dashboard/auth-profile.html',context)


def user_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    UserRegistrations.objects.filter(id=id).delete()
    messages.success(request, 'User has been deleted successfully.')

    return redirect("/auth-list/")


def company_profile(request):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()

    if request.method=="POST":

        company_name  = request.POST.get('company_name')
        slugan  = request.POST.get('slugan')
        email  = request.POST.get('email')
        mobile  = request.POST.get('mobile')
        mobile1  = request.POST.get('mobile1')
        address  = request.POST.get('address')
        about  = request.POST.get('about')
        staring_year  = request.POST.get('staring_year')
        google_map_link  = request.POST.get('google_map_link')
        facebook_link  = request.POST.get('facebook_link')
        twitter_link  = request.POST.get('twitter_link')
        linkedin_link  = request.POST.get('linkedin_link')
        youtube_link  = request.POST.get('youtube_link')
        instragram_link  = request.POST.get('instragram_link')

        document_path = ""
        if bool(request.FILES.get('logo', False)) == True:
            file = request.FILES['logo']   
            if not os.path.exists("logo/"):
                os.mkdir("logo/")

            document_path = default_storage.save("logo/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("logo/")+str(document_path).split("/")[-1] 

        CompanyProfile.objects.create(company_name=company_name,slugan=slugan,email=email,mobile=mobile,
        mobile1=mobile1,address=address,about=about,staring_year=staring_year,google_map_link=google_map_link,
        facebook_link=facebook_link,twitter_link=twitter_link,linkedin_link=linkedin_link,
        youtube_link=youtube_link,instragram_link=instragram_link,logo=document_path)
        messages.success(request, 'Company Registration successfully.')


    context={
        'user':user,
        'get_profile':comprofile,
    }
    return render(request,'realstateapp/dashboard/company-profile-add.html',context)




def company_profile_edit(request,id):
    user = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile      = CompanyProfile.objects.get(id=id)

    if request.method=="POST":

        company_name  = request.POST.get('company_name')
        slugan  = request.POST.get('slugan')
        email  = request.POST.get('email')
        mobile  = request.POST.get('mobile')
        mobile1  = request.POST.get('mobile1')
        address  = request.POST.get('address')
        about  = request.POST.get('about')
        staring_year  = request.POST.get('staring_year')
        google_map_link  = request.POST.get('google_map_link')
        copy_right  = request.POST.get('copy_right')
        facebook_link  = request.POST.get('facebook_link')
        twitter_link  = request.POST.get('twitter_link')
        linkedin_link  = request.POST.get('linkedin_link')
        youtube_link  = request.POST.get('youtube_link')
        instragram_link  = request.POST.get('instragram_link')

        logo = str(getprofile.logo) if getprofile.logo else ""
        if bool(request.FILES.get('logo', False)) == True: 
            if os.path.exists(str(logo)):
                os.remove(str(getprofile.logo))

            file = request.FILES['logo']
            logo = "logo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/logo/'):
                os.mkdir('realstateapp/static/realstateapp/media/logo/') 
            logo = default_storage.save("logo/"+file.name, ContentFile(file.read())) 
            if logo:
                logo = str("logo/")+str(logo).split("/")[-1]

        CompanyProfile.objects.filter(id=id).update(company_name=company_name,slugan=slugan,email=email,mobile=mobile,
        mobile1=mobile1,address=address,about=about,staring_year=staring_year,google_map_link=google_map_link,
        copy_right=copy_right,facebook_link=facebook_link,twitter_link=twitter_link,linkedin_link=linkedin_link,
        youtube_link=youtube_link,instragram_link=instragram_link,logo=logo)
        messages.success(request, 'Profile Updated successfully.')


    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
    }
    return render(request,'realstateapp/dashboard/company-profile-edit.html',context)

def company_list(request):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
    }
    return render(request,'realstateapp/dashboard/company-profile-list.html',context)

def com_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    CompanyProfile.objects.filter(id=id).delete()
    messages.success(request, 'company profile has been deleted successfully.')

    return redirect("/profile-list/")


def amenityadd(request):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)

    if request.method=="POST":
        amenity_name = request.POST.get('amenity_name')

        document_path = ""
        if bool(request.FILES.get('amenity_icon', False)) == True:
            file = request.FILES['amenity_icon']   
            if not os.path.exists("amenity_icon/"):
                os.mkdir("amenity_icon/")

            document_path = default_storage.save("amenity_icon/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("amenity_icon/")+str(document_path).split("/")[-1] 

        Amenity.objects.create(amenity_name=amenity_name,amenity_icon=document_path)
        messages.success(request,'Amenity added successfully')

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
    }
    return render(request,'realstateapp/dashboard/amenity-add.html',context)

def amenitylist(request):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)
    amenitylist   = Amenity.objects.filter(status=1)

    if request.method=="POST":
        amenity_name = request.POST.get('amenity_name')

        document_path = ""
        if bool(request.FILES.get('amenity_icon', False)) == True:
            file = request.FILES['amenity_icon']   
            if not os.path.exists("amenity_icon/"):
                os.mkdir("amenity_icon/")

            document_path = default_storage.save("amenity_icon/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("amenity_icon/")+str(document_path).split("/")[-1] 

        Amenity.objects.create(amenity_name=amenity_name,amenity_icon=document_path)
        messages.success(request,'Amenity added successfully')

    
    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'amenitylist':amenitylist,
    }
    return render(request,'realstateapp/dashboard/amenity-list.html',context)

def amenity_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    Amenity.objects.filter(id=id).delete()
    messages.success(request, 'Amenity has been deleted successfully.')
    return redirect("/amenity-list/")


def amenityedit(request,id):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)
    getamenity   = Amenity.objects.get(id=id)

    if request.method=="POST":
        amenity_name = request.POST.get('amenity_name')

        amenity_icon = str(getamenity.amenity_icon) if getamenity.amenity_icon else ""
        if bool(request.FILES.get('amenity_icon', False)) == True: 
            if os.path.exists(str(amenity_icon)):
                os.remove(str(getamenity.amenity_icon))

            file = request.FILES['amenity_icon']
            amenity_icon = "amenity_icon/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/amenity_icon/'):
                os.mkdir('realstateapp/static/realstateapp/media/amenity_icon/') 
            amenity_icon = default_storage.save("amenity_icon/"+file.name, ContentFile(file.read())) 
            if amenity_icon:
                amenity_icon = str("amenity_icon/")+str(amenity_icon).split("/")[-1] 

        Amenity.objects.filter(id=id).update(amenity_name=amenity_name,amenity_icon=amenity_icon)
        messages.success(request,'Amenity updated successfully')
        return redirect('/amenity-list/')

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getamenity':getamenity,
    }
    return render(request,'realstateapp/dashboard/amenity-edit.html',context)


def facilityadd(request):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)

    if request.method=="POST":
        facility_name = request.POST.get('facility_name')

        document_path = ""
        if bool(request.FILES.get('facility_icon', False)) == True:
            file = request.FILES['facility_icon']   
            if not os.path.exists("facility_icon/"):
                os.mkdir("facility_icon/")

            document_path = default_storage.save("facility_icon/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("facility_icon/")+str(document_path).split("/")[-1] 

        Facility.objects.create(facility_name=facility_name,facility_icon=document_path)
        messages.success(request,'Facility added successfully')

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
    }
    return render(request,'realstateapp/dashboard/facility-add.html',context)

def facilitylist(request):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)
    facilitylist   = Facility.objects.filter(status=1)

    if request.method=="POST":
        facility_name = request.POST.get('facility_name')

        document_path = ""
        if bool(request.FILES.get('facility_icon', False)) == True:
            file = request.FILES['facility_icon']   
            if not os.path.exists("facility_icon/"):
                os.mkdir("facility_icon/")

            document_path = default_storage.save("facility_icon/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("facility_icon/")+str(document_path).split("/")[-1] 

        Facility.objects.create(facility_name=facility_name,facility_icon=document_path)
        messages.success(request,'Facility added successfully')

    
    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'facilitylist':facilitylist,
    }
    return render(request,'realstateapp/dashboard/facility-list.html',context)

def facility_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    Facility.objects.filter(id=id).delete()
    messages.success(request, 'Facility has been deleted successfully.')
    return redirect("/facility-list/")


def facilityedit(request,id):
    user         = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile      = CompanyProfile.objects.all().first()
    getprofile   = CompanyProfile.objects.filter(status=1)
    getfacility   = Facility.objects.get(id=id)

    if request.method=="POST":
        facility_name = request.POST.get('facility_name')

        facility_icon = str(getfacility.facility_icon) if getfacility.facility_icon else ""
        if bool(request.FILES.get('facility_icon', False)) == True: 
            if os.path.exists(str(facility_icon)):
                os.remove(str(getfacility.facility_icon))

            file = request.FILES['facility_icon']
            facility_icon = "facility_icon/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/facility_icon/'):
                os.mkdir('realstateapp/static/realstateapp/media/facility_icon/') 
            facility_icon = default_storage.save("facility_icon/"+file.name, ContentFile(file.read())) 
            if facility_icon:
                facility_icon = str("facility_icon/")+str(facility_icon).split("/")[-1] 

        Facility.objects.filter(id=id).update(facility_name=facility_name,facility_icon=facility_icon)
        messages.success(request,'Facility updated successfully')
        return redirect('/facility-list/')

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getfacility':getfacility,
    }
    return render(request,'realstateapp/dashboard/facility-edit.html',context)

def about(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_mess        = ChairMessage.objects.filter(status=1).first()
    get_team        = TeamMemberInfo.objects.filter(status=1).order_by('member_order')
    gallery         = EventGallery.objects.filter(status=1)
    get_quality     = QualityAdd.objects.filter(status=1).first()
    get_certified   = CertifiedAdd.objects.filter(status=1).first()

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_mess':get_mess,
        'get_team':get_team,
        'gallery':gallery,
        'get_quality':get_quality,
        'get_certified':get_certified,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
    }
    return render(request,'realstateapp/website/about.html',context)


def slider_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    if request.method=="POST":
        title                = request.POST.get('title')
        short_description    = request.POST.get('short_description')
        button_text          = request.POST.get('button_text')
        button_url          = request.POST.get('button_url')
        slider_order         = request.POST.get('slider_order')

        document_path = ""
        if bool(request.FILES.get('slider_banner', False)) == True:
            file = request.FILES['slider_banner']   
            if not os.path.exists("slider_banner/"):
                os.mkdir("slider_banner/")

            document_path = default_storage.save("slider_banner/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("slider_banner/")+str(document_path).split("/")[-1] 

        SliderBanner.objects.create(title=title,slider_banner=document_path,short_description=short_description,
            button_text=button_text,button_url=button_url,slider_order=slider_order
        )
        messages.success(request, 'slider banner has been saved successfully')
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/slider-add.html',context)

def slider_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    sliderlist      = SliderBanner.objects.filter(status=1)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'sliderlist':sliderlist,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/slider-list.html',context)

def slider_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    SliderBanner.objects.filter(id=id).delete()
    messages.success(request, 'Slider has been deleted successfully.')
    return redirect("/slider-list/")

def slider_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    sliderid        = SliderBanner.objects.get(id=id)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    if request.method=="POST":
        title                = request.POST.get('title')
        short_description    = request.POST.get('short_description')
        button_text          = request.POST.get('button_text')
        button_url          = request.POST.get('button_url')
        slider_order         = request.POST.get('slider_order')

        slider_banner = str(sliderid.slider_banner) if sliderid.slider_banner else ""
        if bool(request.FILES.get('slider_banner', False)) == True: 
            if os.path.exists(str(slider_banner)):
                os.remove(str(sliderid.slider_banner))

            file = request.FILES['slider_banner']
            slider_banner = "slider_banner/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/slider_banner/'):
                os.mkdir('realstateapp/static/realstateapp/media/slider_banner/') 
            slider_banner = default_storage.save("slider_banner/"+file.name, ContentFile(file.read())) 
            if slider_banner:
                slider_banner = str("slider_banner/")+str(slider_banner).split("/")[-1] 

        SliderBanner.objects.filter(id=id).update(title=title,slider_banner=slider_banner,short_description=short_description,
            button_text=button_text,button_url=button_url,slider_order=slider_order
        )
        messages.success(request, 'slider banner has been updated successfully')
        return redirect('/slider-list/')
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'sliderid':sliderid,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/slider-edit.html',context)


def message_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    if request.method=="POST":
        mess_name            = request.POST.get('mess_name')
        designation          = request.POST.get('designation')
        chair_message        = request.POST.get('chair_message')
        facebook_link        = request.POST.get('facebook_link')
        twitter_link         = request.POST.get('twitter_link')
        instragram_link      = request.POST.get('instragram_link')

        document_path = ""
        if bool(request.FILES.get('image', False)) == True:
            file = request.FILES['image']   
            if not os.path.exists("message_image/"):
                os.mkdir("message_image/")

            document_path = default_storage.save("message_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("message_image/")+str(document_path).split("/")[-1] 

        ChairMessage.objects.create(name=mess_name,designation=designation,message=chair_message,facebook_link=facebook_link,
            twitter_link=twitter_link,instragram_link=instragram_link,image=document_path,
        )
        messages.success(request,'message added successfully')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/message-add.html',context)


def message_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_mess        = ChairMessage.objects.filter(status=1)

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_mess':get_mess,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/message-list.html',context)


def message_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_mess        = ChairMessage.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        mess_name            = request.POST.get('mess_name')
        designation          = request.POST.get('designation')
        chair_message        = request.POST.get('chair_message')
        facebook_link        = request.POST.get('facebook_link')
        twitter_link         = request.POST.get('twitter_link')
        instragram_link      = request.POST.get('instragram_link')

        image = str(get_mess.image) if get_mess.image else ""
        if bool(request.FILES.get('image', False)) == True: 
            if os.path.exists(str(image)):
                os.remove(str(get_mess.image))

            file = request.FILES['image']
            image = "message_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/message_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/message_image/') 
            image = default_storage.save("message_image/"+file.name, ContentFile(file.read())) 
            if image:
                image = str("message_image/")+str(image).split("/")[-1] 

        ChairMessage.objects.filter(id=id).update(name=mess_name,designation=designation,message=chair_message,facebook_link=facebook_link,
            twitter_link=twitter_link,instragram_link=instragram_link,image=image,
        )
        messages.success(request,'message updated successfully')
        return redirect('/message-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_mess':get_mess,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/message-edit.html',context)


def message_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    ChairMessage.objects.filter(id=id).delete()
    messages.success(request, 'Message has been deleted successfully.')
    return redirect("/message-list/")



def team_member_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        member_name          = request.POST.get('member_name')
        member_disignation   = request.POST.get('member_disignation')
        facebook_link        = request.POST.get('facebook_link')
        twitter_link         = request.POST.get('twitter_link')
        instragram_link      = request.POST.get('instragram_link')
        member_order         = request.POST.get('member_order')

        document_path = ""
        if bool(request.FILES.get('member_image', False)) == True:
            file = request.FILES['member_image']   
            if not os.path.exists("Team_member/"):
                os.mkdir("Team_member/")

            document_path = default_storage.save("Team_member/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("Team_member/")+str(document_path).split("/")[-1] 

        TeamMemberInfo.objects.create(member_name=member_name,member_disignation=member_disignation,facebook_link=facebook_link,
            twitter_link=twitter_link,instragram_link=instragram_link,member_order=member_order,member_image=document_path
            )
        messages.success(request,'Team Member added successfully')
        return redirect('/team-member-add/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/team-member-add.html',context)


def team_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_team        = TeamMemberInfo.objects.filter(status=1).order_by('member_order')

    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    # get_mess        = Message.objects.filter(status=1).first()

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_team':get_team,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/team-member-list.html',context)

def team_member_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_team        = TeamMemberInfo.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        member_name          = request.POST.get('member_name')
        member_disignation   = request.POST.get('member_disignation')
        facebook_link        = request.POST.get('facebook_link')
        twitter_link         = request.POST.get('twitter_link')
        instragram_link      = request.POST.get('instragram_link')
        member_order         = request.POST.get('member_order')

        member_image = str(get_team.member_image) if get_team.member_image else ""
        if bool(request.FILES.get('member_image', False)) == True: 
            if os.path.exists(str(member_image)):
                os.remove(str(get_team.member_image))

            file = request.FILES['member_image']
            member_image = "Team_member/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/Team_member/'):
                os.mkdir('realstateapp/static/realstateapp/media/Team_member/') 
            member_image = default_storage.save("Team_member/"+file.name, ContentFile(file.read())) 
            if member_image:
                member_image = str("Team_member/")+str(member_image).split("/")[-1] 

        TeamMemberInfo.objects.filter(id=id).update(member_name=member_name,member_disignation=member_disignation,facebook_link=facebook_link,
            twitter_link=twitter_link,instragram_link=instragram_link,member_order=member_order,member_image=member_image
            )
        messages.success(request,'Team Member added successfully')
        return redirect('/team-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_team':get_team,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/team-member-edit.html',context)


def team_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    TeamMemberInfo.objects.filter(id=id).delete()
    messages.success(request, 'Team has been deleted successfully.')
    return redirect("/team-list/")

def hot_number_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        title          = request.POST.get('title')
        hot_number     = request.POST.get('hot_number')
      
        HotNumber.objects.create(title=title,number=hot_number)
        messages.success(request,'Number added successfully')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/hot-number-add.html',context)

def hot_number_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    hot_number      = HotNumber.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)



    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'hot_number':hot_number,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/hot-number-list.html',context)


def hot_number_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_number      = HotNumber.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        title          = request.POST.get('title')
        hot_number     = request.POST.get('hot_number')
      
        HotNumber.objects.filter(id=id).update(title=title,number=hot_number)
        messages.success(request,'Number added successfully')
        return redirect('/hot-number-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_number':get_number,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/hot-number-edit.html',context)


def hot_number_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    HotNumber.objects.filter(id=id).delete()
    messages.success(request, 'Number has been deleted successfully.')
    return redirect("/hot-number-list/")


def gallery_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":

        image_list = request.FILES.getlist('picture')
        for image in image_list: 
            picture = ""   
            if not os.path.exists("event_gallery/"):
                os.mkdir("event_gallery/")

            picture = default_storage.save("event_gallery/"+image.name, ContentFile(image.read()))
            if picture:
                picture = str("event_gallery/")+str(picture).split("/")[-1]
                
            EventGallery.objects.create(picture = picture)
      

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/gallery-add.html',context)


def gallery_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_photo       = EventGallery.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":

        picture = str(get_photo.picture) if get_photo.picture else ""
        if bool(request.FILES.get('picture', False)) == True: 
            if os.path.exists(str(picture)):
                os.remove(str(get_photo.picture))

            file = request.FILES['picture']
            picture = "event_gallery/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/event_gallery/'):
                os.mkdir('realstateapp/static/realstateapp/media/event_gallery/') 
            picture = default_storage.save("event_gallery/"+file.name, ContentFile(file.read())) 
            if picture:
                picture = str("event_gallery/")+str(picture).split("/")[-1] 
                
            EventGallery.objects.filter(id=id).update(picture = picture)
      

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_photo':get_photo,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/gallery-edit.html',context)


def gallerylist(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    gallerylist    = EventGallery.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":

        image_list = request.FILES.getlist('picture')
        for image in image_list: 
            picture = ""   
            if not os.path.exists("event_gallery/"):
                os.mkdir("event_gallery/")

            picture = default_storage.save("event_gallery/"+image.name, ContentFile(image.read()))
            if picture:
                picture = str("event_gallery/")+str(picture).split("/")[-1]
                
            EventGallery.objects.create(picture = picture)

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'gallerylist':gallerylist,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/gallery-list.html',context)


def gallery_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    EventGallery.objects.filter(id=id).delete()
    messages.success(request, 'Gallery has been deleted successfully.')
    return redirect("/gallery-list/")


def testimonial_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        test_name            = request.POST.get('test_name')
        profession           = request.POST.get('profession')
        testimonial          = request.POST.get('testimonial')
      

        document_path = ""
        if bool(request.FILES.get('image', False)) == True:
            file = request.FILES['image']   
            if not os.path.exists("testimonial_image/"):
                os.mkdir("testimonial_image/")

            document_path = default_storage.save("testimonial_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("testimonial_image/")+str(document_path).split("/")[-1] 

        TestimonialAdd.objects.create(name=test_name,profession=profession,testimonial=testimonial,image=document_path
        )
        messages.success(request,'Testimonial added successfully')
        return redirect('/testimonial-add/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/testimonial-add.html',context)


def testimonial_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_testi       = TestimonialAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_testi':get_testi,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/testimonial-list.html',context)


def testimonial_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_testi       = TestimonialAdd.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        test_name            = request.POST.get('test_name')
        profession           = request.POST.get('profession')
        testimonial          = request.POST.get('testimonial')
      

        image = str(get_testi.image) if get_testi.image else ""
        if bool(request.FILES.get('image', False)) == True: 
            if os.path.exists(str(image)):
                os.remove(str(get_testi.image))

            file = request.FILES['image']
            image = "testimonial_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/testimonial_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/testimonial_image/') 
            image = default_storage.save("testimonial_image/"+file.name, ContentFile(file.read())) 
            if image:
                image = str("testimonial_image/")+str(image).split("/")[-1] 

        TestimonialAdd.objects.filter(id=id).update(name=test_name,profession=profession,testimonial=testimonial,image=image
        )
        messages.success(request,'Testimonial updated successfully')
        return redirect('/testimonial-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_testi':get_testi,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/testimonial-edit.html',context)

def testimonial_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    TestimonialAdd.objects.filter(id=id).delete()
    messages.success(request, 'Testimonial has been deleted successfully.')
    return redirect("/testimonial-list/")


def quality_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        quality_title        = request.POST.get('quality_title')
        quality_text         = request.POST.get('quality_text')
      

        document_path = ""
        if bool(request.FILES.get('image', False)) == True:
            file = request.FILES['image']   
            if not os.path.exists("quality_image/"):
                os.mkdir("quality_image/")

            document_path = default_storage.save("quality_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("quality_image/")+str(document_path).split("/")[-1] 

        QualityAdd.objects.create(quality_title=quality_title,quality_text=quality_text,image=document_path
        )
        messages.success(request,'Quality added successfully')
        return redirect('/quality-add/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/quality-add.html',context)


def quality_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    quality         = QualityAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'quality':quality,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/quality-list.html',context)


def quality_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_quality     = QualityAdd.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        quality_title        = request.POST.get('quality_title')
        quality_text         = request.POST.get('quality_text')
      

        image = str(get_quality.image) if get_quality.image else ""
        if bool(request.FILES.get('image', False)) == True: 
            if os.path.exists(str(image)):
                os.remove(str(get_quality.image))

            file = request.FILES['image']
            image = "quality_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/quality_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/quality_image/') 
            image = default_storage.save("quality_image/"+file.name, ContentFile(file.read())) 
            if image:
                image = str("quality_image/")+str(image).split("/")[-1] 

        QualityAdd.objects.filter(id=id).update(quality_title=quality_title,quality_text=quality_text,image=image
        )
        messages.success(request,'Quality updated successfully')
        return redirect('/quality-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_quality':get_quality,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/quality-edit.html',context)

def quality_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    QualityAdd.objects.filter(id=id).delete()
    messages.success(request, 'Quality has been deleted successfully.')
    return redirect("/quality-list/")


def certified_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        certified_title        = request.POST.get('certified_title')
        certified_text         = request.POST.get('certified_text')
      

        CertifiedAdd.objects.create(certified_title=certified_title,certified_text=certified_text)
        messages.success(request,'Certified added successfully')
        return redirect('/certified-add/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/certified-add.html',context)

def certified_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    if request.method=="POST":
        certified_title        = request.POST.get('certified_title')
        certified_text         = request.POST.get('certified_text')
      

        CertifiedAdd.objects.filter(id=id).update(certified_title=certified_title,certified_text=certified_text)
        messages.success(request,'Certified updated successfully')
        return redirect('/certified-list/')

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/certified-edit.html',context)


def certified_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/certified-list.html',context)

def certified_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    CertifiedAdd.objects.filter(id=id).delete()
    messages.success(request, 'Certified has been deleted successfully.')
    return redirect("/certified-list/")


def testimonial(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    testimonial     = TestimonialAdd.objects.filter(status=1)

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        'client_testi':testimonial,
    }
    return render(request,'realstateapp/website/testimonial.html',context)




def contact(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    testimonial     = TestimonialAdd.objects.filter(status=1)
    
    
    if request.method == "POST":
        name       = request.POST.get('name')
        email       = request.POST.get('email')
        property_plot_type       = request.POST.get('property_plot_type')
        location           = request.POST.get('location')
        apartment_size           = request.POST.get('apartment_size')
        message            = request.POST.get('message')
       
        ContactMessage.objects.create(
            name=name,
            email=email,
            property_plot_type=property_plot_type,
            location=location,
            apartment_size=apartment_size,
            message=message,
        )
   

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        'client_testi':testimonial,
    }
    return render(request,'realstateapp/website/contact.html',context)


def client_contact(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/client-contact-list.html',context)

def terms_conditions_dash(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        title             = request.POST.get('title')
        terms_conditions  = request.POST.get('terms_conditions')

        document_path = ""
        if bool(request.FILES.get('picture', False)) == True:
            file = request.FILES['picture']   
            if not os.path.exists("testimonial_image/"):
                os.mkdir("testimonial_image/")

            document_path = default_storage.save("testimonial_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("testimonial_image/")+str(document_path).split("/")[-1] 

        TermsConditions.objects.create(title=title,terms_conditions=terms_conditions,picture=document_path)
        messages.success(request,'Terms & Conditions added successfully')


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/terms-conditions-add.html',context)

def terms_conditions_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_terms       = TermsConditions.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        title             = request.POST.get('title')
        terms_conditions  = request.POST.get('terms_conditions')

        picture = str(get_terms.picture) if get_terms.picture else ""
        if bool(request.FILES.get('picture', False)) == True: 
            if os.path.exists(str(picture)):
                os.remove(str(get_terms.picture))

            file = request.FILES['picture']
            picture = "testimonial_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/testimonial_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/testimonial_image/') 
            picture = default_storage.save("testimonial_image/"+file.name, ContentFile(file.read())) 
            if picture:
                picture = str("testimonial_image/")+str(picture).split("/")[-1]  

        TermsConditions.objects.filter(id=id).update(title=title,terms_conditions=terms_conditions,picture=picture)
        messages.success(request,'Terms & Conditions updated successfully')


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_terms':get_terms,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/terms-conditions-edit.html',context)

def terms_conditions_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_terms       = TermsConditions.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_terms':get_terms,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/terms-conditions-list.html',context)

def terms_conditions_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    TermsConditions.objects.filter(id=id).delete()
    messages.success(request, 'Terms & Conditions has been deleted successfully.')
    return redirect("/terms-conditions-list/")


def terms_conditions(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_terms       = TermsConditions.objects.filter(status=1).first()
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_terms':get_terms,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/terms-conditions.html',context)


def privacy_policy(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_privacy     = PrivacyPolicy.objects.filter(status=1).first()
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_privacy':get_privacy,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/privacy-policy.html',context)


def privacy_policy_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        title             = request.POST.get('title')
        privacy_policy    = request.POST.get('privacy_policy')

        document_path = ""
        if bool(request.FILES.get('picture', False)) == True:
            file = request.FILES['picture']   
            if not os.path.exists("privacy_image/"):
                os.mkdir("privacy_image/")

            document_path = default_storage.save("privacy_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("privacy_image/")+str(document_path).split("/")[-1] 

        PrivacyPolicy.objects.create(title=title,privacy_policy=privacy_policy,picture=document_path)
        messages.success(request,'Privacy Policy added successfully')


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/privacy-policy-add.html',context)

def privacy_policy_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        title             = request.POST.get('title')
        privacy_policy    = request.POST.get('privacy_policy')

        picture = str(get_pp.picture) if get_pp.picture else ""
        if bool(request.FILES.get('picture', False)) == True: 
            if os.path.exists(str(picture)):
                os.remove(str(get_pp.picture))

            file = request.FILES['picture']
            picture = "privacy_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/privacy_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/privacy_image/') 
            picture = default_storage.save("privacy_image/"+file.name, ContentFile(file.read())) 
            if picture:
                picture = str("privacy_image/")+str(picture).split("/")[-1]  

        PrivacyPolicy.objects.filter(id=id).update(title=title,privacy_policy=privacy_policy,picture=picture)
        messages.success(request,'Privacy Policy updated successfully')


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/privacy-policy-edit.html',context)


def privacy_policy_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)



    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/privacy-policy-list.html',context)

def privacy_policy_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    PrivacyPolicy.objects.filter(id=id).delete()
    messages.success(request, 'Privacy Policy has been deleted successfully.')
    return redirect("/privacy-policy-list/")


def faq_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    if request.method=="POST":
        question  = request.POST.get('question')
        answer    = request.POST.get('answer')

        Faq.objects.create(question=question,answer=answer)
        messages.success(request,'faq has been saved successfylly')




    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/faq-add.html',context)

def faq_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    if request.method=="POST":
        question  = request.POST.get('question')
        answer    = request.POST.get('answer')

        Faq.objects.filter(id=id).update(question=question,answer=answer)
        messages.success(request,'faq has been updated successfylly')
        return redirect('/faq-list/')




    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/faq-edit.html',context)

def faq_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/faq-list.html',context)


def faq_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    Faq.objects.filter(id=id).delete()
    messages.success(request, 'faq has been deleted successfully.')
    return redirect("/faq-list/")


def faq(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_privacy     = PrivacyPolicy.objects.filter(status=1).first()
    get_faq         = Faq.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_privacy':get_privacy,
        'get_faq':get_faq,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/faq.html',context)


def service_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        service_name   = request.POST.get('service_name')

        ServiceEntry.objects.create(service_name=service_name)
        messages.success(request,'Service added successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-add.html',context)

def service_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-list.html',context)

def service_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_service     = ServiceEntry.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        service_name   = request.POST.get('service_name')

        ServiceEntry.objects.filter(id=id).update(service_name=service_name)
        messages.success(request,'Service updated successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_service':get_service,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-edit.html',context)


def service_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    ServiceEntry.objects.filter(id=id).delete()
    messages.success(request, 'Service has been deleted successfully.')
    return redirect("/service-list/")


def service_details_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        service_name          = request.POST.get('service_name')
        service_title         = request.POST.get('service_title')
        service_description   = request.POST.get('service_description')

        document_path = ""
        if bool(request.FILES.get('service_banner', False)) == True:
            file = request.FILES['service_banner']   
            if not os.path.exists("service_banner/"):
                os.mkdir("service_banner/")

            document_path = default_storage.save("service_banner/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("service_banner/")+str(document_path).split("/")[-1]

        document = ""
        if bool(request.FILES.get('service_image', False)) == True:
            file = request.FILES['service_image']   
            if not os.path.exists("service_image/"):
                os.mkdir("service_image/")

            document = default_storage.save("service_image/"+file.name, ContentFile(file.read()))
            if document:
                document = str("service_image/")+str(document).split("/")[-1] 


        ServiceDetails.objects.create(service_name_id=service_name,service_title=service_title,
        service_description=service_description,service_banner=document_path,service_image=document)
        messages.success(request,'Service  Details added successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-details-add.html',context)


def service_details_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    ser_details     = ServiceDetails.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        service_name          = request.POST.get('service_name')
        service_title         = request.POST.get('service_title')
        service_description   = request.POST.get('service_description')

        service_banner = str(ser_details.service_banner) if ser_details.service_banner else ""
        if bool(request.FILES.get('service_banner', False)) == True: 
            if os.path.exists(str(service_banner)):
                os.remove(str(ser_details.service_banner))

            file = request.FILES['service_banner']
            service_banner = "service_banner/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/service_banner/'):
                os.mkdir('realstateapp/static/realstateapp/media/service_banner/') 
            service_banner = default_storage.save("service_banner/"+file.name, ContentFile(file.read())) 
            if service_banner:
                service_banner = str("service_banner/")+str(service_banner).split("/")[-1]  
            

        service_image = str(ser_details.service_image) if ser_details.service_image else ""
        if bool(request.FILES.get('service_image', False)) == True: 
            if os.path.exists(str(service_image)):
                os.remove(str(ser_details.service_image))

            file = request.FILES['service_image']
            service_image = "service_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/service_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/service_image/') 
            service_image = default_storage.save("service_image/"+file.name, ContentFile(file.read())) 
            if service_image:
                service_image = str("service_image/")+str(service_image).split("/")[-1] 


        ServiceDetails.objects.filter(id=id).update(service_name_id=service_name,service_title=service_title,
        service_description=service_description,service_banner=service_banner,service_image=service_image)
        messages.success(request,'Service  Details updated successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        'ser_details':ser_details,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-details-edit.html',context)



def service_details_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    ser_details     = ServiceDetails.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        'ser_details':ser_details,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/service-details-list.html',context)

def service_details_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    ServiceDetails.objects.filter(id=id).delete()
    messages.success(request, 'Service has been deleted successfully.')
    return redirect("/service-details-list/")


def service_details(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    getservice      = ServiceEntry.objects.filter(status=1)
    serdetails      = ServiceDetails.objects.get(id=id)
    hot_number      = HotNumber.objects.filter(status=1)
    get_testi       = TestimonialAdd.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'getservice':getservice,
        'serdetails':serdetails,
        'hot_number':hot_number,
        'get_testi':get_testi,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/service-details.html',context)


def sister_company(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    getservice      = ServiceEntry.objects.filter(status=1)
    hot_number      = HotNumber.objects.filter(status=1)
    get_testi       = TestimonialAdd.objects.filter(status=1)
    concern_entry   = SisternConcernEntry.objects.all()
    get_detail      = SisternConcernDetails.objects.get(sister_concern_name_id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'getservice':getservice,
        'hot_number':hot_number,
        'get_testi':get_testi,
        'concern_entry':concern_entry,
        'get_detail':get_detail,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/website/sister-company.html',context)


def sister_concern_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        sister_concern_name   = request.POST.get('sister_concern_name')

        SisternConcernEntry.objects.create(sister_concern_name=sister_concern_name)
        messages.success(request,'Sister Concern added successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-add.html',context)

def sister_concern_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_sister      = SisternConcernEntry.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_sister':get_sister,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-list.html',context)

def sister_concern_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_sister      = SisternConcernEntry.objects.get(id=id)
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        sister_concern_name   = request.POST.get('sister_concern_name')

        SisternConcernEntry.objects.filter(id=id).update(sister_concern_name=sister_concern_name)
        messages.success(request,'Sister Concern updated successfully')
        return redirect('/sister-concern-list/')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_sister':get_sister,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-edit.html',context)

def sister_concern_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    SisternConcernEntry.objects.filter(id=id).delete()
    messages.success(request, 'sister concern has been deleted successfully.')
    return redirect("/sister-concern-list/")



def sister_concern_details_add(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    get_sister      = SisternConcernEntry.objects.filter(status=1)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        sister_concern_name   = request.POST.get('sister_concern_name')
        address               = request.POST.get('address')
        mobile                = request.POST.get('mobile')
        email                 = request.POST.get('email')
        facebook_link         = request.POST.get('facebook_link')
        twitter_link          = request.POST.get('twitter_link')
        linkedin_link         = request.POST.get('linkedin_link')
        youtube_link          = request.POST.get('youtube_link')
        service_description   = request.POST.get('service_description')

        document = ""
        if bool(request.FILES.get('sister_concern_banner', False)) == True:
            file = request.FILES['sister_concern_banner']   
            if not os.path.exists("sister_concern_banner/"):
                os.mkdir("sister_concern_banner/")

            document = default_storage.save("sister_concern_banner/"+file.name, ContentFile(file.read()))
            if document:
                document = str("sister_concern_banner/")+str(document).split("/")[-1]
        
        document_path = ""
        if bool(request.FILES.get('sister_concern_image', False)) == True:
            file = request.FILES['sister_concern_image']   
            if not os.path.exists("sister_concern_image/"):
                os.mkdir("sister_concern_image/")

            document_path = default_storage.save("sister_concern_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("sister_concern_image/")+str(document_path).split("/")[-1] 
            

       

        SisternConcernDetails.objects.create(sister_concern_name_id=sister_concern_name,address=address,
            mobile=mobile,email=email,facebook_link=facebook_link,twitter_link=twitter_link,
            linkedin_link=linkedin_link,youtube_link=youtube_link,service_description=service_description,
            sister_concern_banner=document,sister_concern_image=document_path
        )
        messages.success(request,'sister concern  Details added successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        'get_sister':get_sister,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-details-add.html',context)


def sister_concern_details_list(request):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    get_sister      = SisternConcernEntry.objects.filter(status=1)
    sister_concern  = SisternConcernDetails.objects.filter(status=1)
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)


    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        'get_sister':get_sister,
        'sister_concern':sister_concern,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-details-list.html',context)


def sister_concern_details_edit(request,id):
    comprofile      = CompanyProfile.objects.all().first()
    get_slider      = SliderBanner.objects.filter(status=1).order_by('slider_order')
    get_all         = PropertyEntry.objects.filter(status=1)
    getupcoming     = PropertyEntry.objects.filter(status=1,property_catagory=1)
    get_on          = PropertyEntry.objects.filter(status=1,property_catagory=2)
    get_com         = PropertyEntry.objects.filter(status=1,property_catagory=3)
    phase           = PhaseAdd.objects.filter(status=1)
    add_property    = PropertyType.objects.filter(status=1)
    get_location    = LocationAdd.objects.filter(status=1)
    get_certified   = CertifiedAdd.objects.filter(status=1)
    get_list        = ContactMessage.objects.filter(status=1)
    get_pp          = PrivacyPolicy.objects.filter(status=1)
    get_faq         = Faq.objects.filter(status=1)
    get_service     = ServiceEntry.objects.filter(status=1)
    get_sister      = SisternConcernEntry.objects.filter(status=1)
    get_concern_details    = SisternConcernDetails.objects.get(id=id)
    # concern_entry   = SisternConcernEntry.objects.all()
    # hot_number      = HotNumber.objects.filter(status=1)
    # testimonial     = TestimonialAdd.objects.filter(status=1)

    if request.method=="POST":
        sister_concern_name   = request.POST.get('sister_concern_name')
        address               = request.POST.get('address')
        mobile                = request.POST.get('mobile')
        email                 = request.POST.get('email')
        facebook_link         = request.POST.get('facebook_link')
        twitter_link          = request.POST.get('twitter_link')
        linkedin_link         = request.POST.get('linkedin_link')
        youtube_link          = request.POST.get('youtube_link')
        service_description   = request.POST.get('service_description')

        sister_concern_banner = str(get_concern_details.sister_concern_banner) if get_concern_details.sister_concern_banner else ""
        if bool(request.FILES.get('sister_concern_banner', False)) == True: 
            if os.path.exists(str(sister_concern_banner)):
                os.remove(str(get_concern_details.sister_concern_banner))

            file = request.FILES['sister_concern_banner']
            sister_concern_banner = "sister_concern_banner/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/sister_concern_banner/'):
                os.mkdir('realstateapp/static/realstateapp/media/sister_concern_banner/') 
            sister_concern_banner = default_storage.save("sister_concern_banner/"+file.name, ContentFile(file.read())) 
            if sister_concern_banner:
                sister_concern_banner = str("sister_concern_banner/")+str(sister_concern_banner).split("/")[-1]


        sister_concern_image = str(get_concern_details.sister_concern_image) if get_concern_details.sister_concern_image else ""
        if bool(request.FILES.get('sister_concern_image', False)) == True: 
            if os.path.exists(str(sister_concern_image)):
                os.remove(str(get_concern_details.sister_concern_image))

            file = request.FILES['sister_concern_image']
            sister_concern_image = "sister_concern_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/sister_concern_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/sister_concern_image/') 
            sister_concern_image = default_storage.save("sister_concern_image/"+file.name, ContentFile(file.read())) 
            if sister_concern_image:
                sister_concern_image = str("sister_concern_image/")+str(sister_concern_image).split("/")[-1]    

        SisternConcernDetails.objects.filter(id=id).update(sister_concern_name_id=sister_concern_name,address=address,
            mobile=mobile,email=email,facebook_link=facebook_link,twitter_link=twitter_link,
            linkedin_link=linkedin_link,youtube_link=youtube_link,service_description=service_description,
            sister_concern_banner=sister_concern_banner,sister_concern_image=sister_concern_image
        )
        messages.success(request,'sister concern  Details updated successfully')
    

    context ={
        'get_profile':comprofile,
        'get_slider':get_slider,
        'get_all':get_all,
        'getupcoming':getupcoming,
        'get_on':get_on,
        'get_com':get_com,
        'get_phase':phase,
        'add_property':add_property,
        'get':get_location,
        'get_certified':get_certified,
        'get_list':get_list,
        'get_pp':get_pp,
        'get_faq':get_faq,
        'get_service':get_service,
        'get_sister':get_sister,
        'get_concern_details':get_concern_details,
        # 'concern_entry':concern_entry,
        # 'hot_number':hot_number,
        # 'client_testi':testimonial,
        # 'get_mess':get_mess,
    }
    return render(request,'realstateapp/dashboard/sister-concern-details-edit.html',context)


def sister_concern_details_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    SisternConcernDetails.objects.filter(id=id).delete()
    messages.success(request, 'sister concern has been deleted successfully.')
    return redirect("/sister-concern-details-list/")