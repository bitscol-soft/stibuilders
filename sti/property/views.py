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
# Create your views here.
def cretepro(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    get_last           = PropertyEntry.objects.filter(date = datetime.datetime.now()).last()
    property_type      = PropertyType.objects.filter(status=1)
    cons_status        = ConstructionStatus.objects.filter(status=1)
    sales_status       = SalesStatus.objects.filter(status=1)
    amenity            = Amenity.objects.filter(status=1)
    facility           = Facility.objects.filter(status=1)
    getproject         = ProjectAdd.objects.filter(status=1)
    getphase           = PhaseAdd.objects.filter(status=1)
    getlocation        = LocationAdd.objects.filter(status=1)
    


    # ====plot land =======
    getsclale          = MeasurementScale.objects.filter(status=1)
    getlandstatus      = PlotLandStatus.objects.filter(status=1)
    landfacility       = LandFacilityEntry.objects.all()
    getplotproject     = ProjectPlotLand.objects.all()

    if request.method=="POST":
        date                 = datetime.datetime.now()

        property_catagory    = request.POST.get('property_catagory')
        property_name        = request.POST.get('property_name')
        project_name         = request.POST.get('project_name')
        selling_price        = request.POST.get('selling_price')
        property_area        = request.POST.get('property_area')
        bed                  = request.POST.get('bed')
        bath                 = request.POST.get('bath')
        number_of_belcony    = request.POST.get('number_of_belcony')
        construction_status  = request.POST.get('construction_status')
        sales_type           = request.POST.get('sales_type')
        location_map         = request.POST.get('location_map')
        kitchen_space        = request.POST.get('kitchen_space')
        daining_space        = request.POST.get('daining_space')
        flat_apartment_no    = request.POST.get('flat_apartment_no')
        address              = request.POST.get('address')
        property_type        = request.POST.get('property_type')
        choose_phase         = request.POST.get('choose_phase')
        location             = request.POST.get('location')


        property_video_rul   = request.POST.getlist('property_video_rul')

        property_owner_name  = request.POST.getlist('property_owner_name')
        property_ownership   = request.POST.getlist('property_ownership')

        amenity_id           = request.POST.getlist('amenity_id')
        facility_id          = request.POST.getlist('facility_id')
   
        month  = datetime.datetime.now().month
        day    = datetime.datetime.now().day
        if len(str(month)) == 1:
            month = "0"+str(month)
        if len(str(day)) == 1:
            day = "0"+str(day)
        prefix = str(datetime.datetime.now().year)+str(month)+str(day)
        if get_last:
            property_id     = int(get_last.property_id)+1
        else:
            property_id     = prefix+"1"
        
        document_path = ""
        if bool(request.FILES.get('property_image', False)) == True:
            file = request.FILES['property_image']   
            if not os.path.exists("property_image/"):
                os.mkdir("property_image/")

            document_path = default_storage.save("property_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("property_image/")+str(document_path).split("/")[-1] 
        
        documentpath = ""
        if bool(request.FILES.get('property_banner', False)) == True:
            file = request.FILES['property_banner']   
            if not os.path.exists("property_banner/"):
                os.mkdir("property_banner/")

            documentpath = default_storage.save("property_banner/"+file.name, ContentFile(file.read()))
            if documentpath:
                documentpath = str("property_banner/")+str(documentpath).split("/")[-1]
        
        flor_plan = ""
        if bool(request.FILES.get('flor_plan', False)) == True:
            file = request.FILES['flor_plan']   
            if not os.path.exists("flor_plan/"):
                os.mkdir("flor_plan/")

            flor_plan = default_storage.save("flor_plan/"+file.name, ContentFile(file.read()))
            if flor_plan:
                flor_plan = str("flor_plan/")+str(flor_plan).split("/")[-1]
        
        
        brochure = ""
        if bool(request.FILES.get('brochure', False)) == True:
            file = request.FILES['brochure']   
            if not os.path.exists("brochure/"):
                os.mkdir("brochure/")

            brochure = default_storage.save("brochure/"+file.name, ContentFile(file.read()))
            if brochure:
                brochure = str("brochure/")+str(brochure).split("/")[-1]
                

        propertyid = PropertyEntry.objects.create(date=date,property_id=property_id,property_catagory=property_catagory,
            property_name=property_name,project_name=project_name,selling_price=selling_price,
            property_area=property_area,bed=bed,bath=bath,number_of_belcony=number_of_belcony,construction_status=construction_status,
            sales_type=sales_type,location_map=location_map,kitchen_space=kitchen_space,daining_space=daining_space,
            flat_apartment_no=flat_apartment_no,property_image=document_path,property_banner=documentpath,
            brochure=brochure,flor_plan=flor_plan,address=address,property_type=property_type,choose_phase=choose_phase,
            location=location,
            created_by_id=int(request.session['userid'])
        )

        image_list = request.FILES.getlist('property_photo')
        for image in image_list: 
            property_photo = ""   
            if not os.path.exists("property_image/"):
                os.mkdir("property_image/")

            property_photo = default_storage.save("property_image/"+image.name, ContentFile(image.read()))
            if property_photo:
                property_photo = str("property_image/")+str(property_photo).split("/")[-1]
                
            PropertyPhoto.objects.create(property_photo = property_photo, property_id = propertyid)
        
        for amenity_id in amenity_id:
            PropertyAmenity.objects.create(property_id = propertyid,amenity_name_id=amenity_id)

        for facility_id in facility_id:
            PropertyFacility.objects.create(property_id = propertyid,facility_name_id=facility_id)
        
        for provideo_rul in property_video_rul: 
        
            PropertyVideo.objects.create(
                property_video_rul = provideo_rul,
                property_id = propertyid
            )
        
        for proowner, ownership in zip(property_owner_name,property_ownership): 
        
            PropertyOwnership.objects.create(
                property_owner_name = proowner,  property_ownership = ownership,
                property_id = propertyid
            )


        messages.success(request, 'Property has been saved successfully.')
        return redirect("/property/create-property/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,'property_type':property_type,
        'cons_status':cons_status,'sales_status':sales_status,
        'amenity':amenity,'facility':facility,'getproject':getproject,
        'getsclale':getsclale,
        'getlandstatus':getlandstatus,'landfacility':landfacility,
        'getplotproject':getplotproject,'getphase':getphase,'getlocation':getlocation,
    }
    return render(request,'property/dashboard/create-property.html',context)

def propertylist(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    getproperty        = PropertyEntry.objects.filter(status=1)

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getproperty':getproperty,
    }

    return render(request,'property/dashboard/property-list.html',context)





def property_edit(request,property_id):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    property_type      = PropertyType.objects.filter(status=1)
    cons_status        = ConstructionStatus.objects.filter(status=1)
    sales_status       = SalesStatus.objects.filter(status=1)
    amenity            = Amenity.objects.filter(status=1)
    facility           = Facility.objects.filter(status=1)
    getproject         = ProjectAdd.objects.filter(status=1)
    getproperty        = PropertyEntry.objects.get(property_id=property_id)
    get_image          = PropertyPhoto.objects.filter(property_id=property_id)
    get_video          = PropertyVideo.objects.filter(property_id=property_id)
    get_owner          = PropertyOwnership.objects.filter(property_id=property_id)
    get_amenity        = PropertyAmenity.objects.filter(property_id=property_id)
    get_facility       = PropertyFacility.objects.filter(property_id=property_id)
    getphase           = PhaseAdd.objects.filter(status=1)
    getlocation        = LocationAdd.objects.filter(status=1)

    property_video_rul       = request.POST.getlist('property_video_rul')
    property_owner_name      = request.POST.getlist('property_owner_name')
    property_ownership       = request.POST.getlist('property_ownership')

    amenity_id            = request.POST.getlist('amenity_id')
    facility_id            = request.POST.getlist('facility_id')
  


    if request.method=="POST":
        property_catagory    = request.POST.get('property_catagory')
        property_name        = request.POST.get('property_name')
        project_name        = request.POST.get('project_name')
        selling_price        = request.POST.get('selling_price')
        property_area        = request.POST.get('property_area')
        bed                  = request.POST.get('bed')
        bath                 = request.POST.get('bath')
        number_of_belcony    = request.POST.get('number_of_belcony')
        construction_status  = request.POST.get('construction_status')
        sales_type           = request.POST.get('sales_status')
        location_map         = request.POST.get('location_map')
        kitchen_space        = request.POST.get('kitchen_space')
        daining_space        = request.POST.get('daining_space')
        flat_apartment_no    = request.POST.get('flat_apartment_no')
        choose_phase         = request.POST.get('choose_phase')
        property_type        = request.POST.get('property_type')
        location             = request.POST.get('location')
        address              = request.POST.get('address')


        property_image = str(getproperty.property_image) if getproperty.property_image else ""
        if bool(request.FILES.get('property_image', False)) == True: 
            if os.path.exists(str(property_image)):
                os.remove(str(getproperty.property_image))

            file = request.FILES['property_image']
            property_image = "property_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/property_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/property_image/') 
            property_image = default_storage.save("property_image/"+file.name, ContentFile(file.read())) 
            if property_image:
                property_image = str("property_image/")+str(property_image).split("/")[-1] 


        property_banner = str(getproperty.property_banner) if getproperty.property_banner else ""
        if bool(request.FILES.get('property_banner', False)) == True: 
            if os.path.exists(str(property_banner)):
                os.remove(str(getproperty.property_banner))

            file = request.FILES['property_banner']
            property_banner = "property_banner/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/property_banner/'):
                os.mkdir('realstateapp/static/realstateapp/media/property_banner/') 
            property_banner = default_storage.save("property_banner/"+file.name, ContentFile(file.read())) 
            if property_banner:
                property_banner = str("property_banner/")+str(property_banner).split("/")[-1]
        
        flor_plan = str(getproperty.flor_plan) if getproperty.flor_plan else ""
        if bool(request.FILES.get('flor_plan', False)) == True: 
            if os.path.exists(str(flor_plan)):
                os.remove(str(getproperty.flor_plan))

            file = request.FILES['flor_plan']
            flor_plan = "flor_plan/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/flor_plan/'):
                os.mkdir('realstateapp/static/realstateapp/media/flor_plan/') 
            flor_plan = default_storage.save("flor_plan/"+file.name, ContentFile(file.read())) 
            if flor_plan:
                flor_plan = str("flor_plan/")+str(flor_plan).split("/")[-1]
        
        brochure = str(getproperty.brochure) if getproperty.brochure else ""
        if bool(request.FILES.get('brochure', False)) == True: 
            if os.path.exists(str(brochure)):
                os.remove(str(getproperty.brochure))

            file = request.FILES['brochure']
            brochure = "brochure/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/brochure/'):
                os.mkdir('realstateapp/static/realstateapp/media/brochure/') 
            brochure = default_storage.save("brochure/"+file.name, ContentFile(file.read())) 
            if brochure:
                brochure = str("brochure/")+str(brochure).split("/")[-1]
        
        

        PropertyEntry.objects.filter(property_id=property_id).update(property_catagory=property_catagory,
            property_name=property_name,project_name=project_name,selling_price=selling_price,
            property_area=property_area,bed=bed,bath=bath,number_of_belcony=number_of_belcony,construction_status=construction_status,
            sales_type=sales_type,location_map=location_map,kitchen_space=kitchen_space,daining_space=daining_space,
            flat_apartment_no=flat_apartment_no,property_image=property_image,property_banner=property_banner,
            brochure=brochure,flor_plan=flor_plan,choose_phase=choose_phase,property_type=property_type,
            location=location,address=address,
            created_by_id=int(request.session['userid'])
        )

        image_list = request.FILES.getlist('property_photo')
        for image in image_list: 
            property_photo = ""   
            if not os.path.exists("property_photo/"):
                os.mkdir("property_photo/")

            property_photo = default_storage.save("property_photo/"+image.name, ContentFile(image.read()))
            if property_photo:
                property_photo = str("property_photo/")+str(property_photo).split("/")[-1]

            PropertyPhoto.objects.filter(property_id=property_id).create(property_photo = property_photo,property_id=property_id)

        PropertyVideo.objects.filter(property_id=property_id).delete()
        for provideo_rul in property_video_rul: 
        
            PropertyVideo.objects.filter(property_id=property_id).create(
                property_video_rul = provideo_rul,
                property_id = property_id
            )
        
        PropertyOwnership.objects.filter(property_id=property_id).delete()
        for proowner, ownership in zip(property_owner_name,property_ownership): 
        
            PropertyOwnership.objects.filter(property_id=property_id).create(
                property_owner_name = proowner,  property_ownership = ownership,
                property_id = property_id
            )
        # PropertyAmenity.objects.filter(property_id=property_id).delete()
        for amenity_id in amenity_id:
            PropertyAmenity.objects.filter(property_id=property_id).create(property_id = property_id,amenity_name_id=amenity_id)
        
        for facility_id in facility_id:
            PropertyFacility.objects.filter(property_id=property_id).create(property_id = property_id,facility_name_id=facility_id)


        messages.success(request, 'Property has been updated successfully.')
        return redirect("/property/property-list/")
        

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,'property_type':property_type,
        'cons_status':cons_status,'sales_status':sales_status,
        'amenity':amenity,'facility':facility,'getproject':getproject,
        'getproperty':getproperty,
        'getproperty':getproperty,'get_image':get_image,'get_video':get_video,
        'get_owner':get_owner,'get_amenity':get_amenity,'get_facility':get_facility,
        'getphase':getphase,'getlocation':getlocation,
    }
    return render(request,'property/dashboard/property-edit.html',context)



def property_photo_edit(request,id):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    property_type      = PropertyType.objects.filter(status=1)
    cons_status        = ConstructionStatus.objects.filter(status=1)
    sales_status       = SalesStatus.objects.filter(status=1)
    amenity            = Amenity.objects.filter(status=1)
    facility           = Facility.objects.filter(status=1)
    getproject         = ProjectAdd.objects.filter(status=1)
    get_image          = PropertyPhoto.objects.get(id=id)
    getphase           = PhaseAdd.objects.filter(status=1)
    getlocation        = LocationAdd.objects.filter(status=1)

    if request.method=="POST":
     
        property_photo = str(get_image.property_photo) if get_image.property_photo else ""
        if bool(request.FILES.get('property_photo', False)) == True: 
            if os.path.exists(str(property_photo)):
                os.remove(str(get_image.property_photo))

            file = request.FILES['property_photo']
            property_photo = "property_photo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/property_photo/'):
                os.mkdir('realstateapp/static/realstateapp/media/property_photo/') 
            property_photo = default_storage.save("property_photo/"+file.name, ContentFile(file.read())) 
            if property_photo:
                property_photo = str("property_photo/")+str(property_photo).split("/")[-1]
        
        PropertyPhoto.objects.filter(id=id).update(property_photo = property_photo)
        

        messages.success(request, 'Property photo has been updated successfully.')

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,'property_type':property_type,
        'cons_status':cons_status,'sales_status':sales_status,
        'amenity':amenity,'facility':facility,'getproject':getproject,
        'get_image':get_image,
        'getphase':getphase,'getlocation':getlocation,
    }
    return render(request,'property/dashboard/property-photo-edit.html',context)


def plotland_add(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    get_last           = PlotLandEntry.objects.filter(date = datetime.datetime.now()).last()
    getsclale          = MeasurementScale.objects.filter(status=1)
    getlandstatus      = PlotLandStatus.objects.filter(status=1)
    landfacility       = LandFacilityEntry.objects.all()
    getplotproject     = ProjectPlotLand.objects.all()

    print("data", landfacility)


    if request.method=="POST":
        date                 = datetime.datetime.now()
        developer_name       = request.POST.get('developer_name')
        block                = request.POST.get('block')
        map_url              = request.POST.get('map_url')
        sector               = request.POST.get('sector')
        road_no              = request.POST.get('road_no')
        plot_no              = request.POST.get('plot_no')
        land_size            = request.POST.get('land_size')
        measurement_scale    = request.POST.get('measurement_scale')
        plot_land_status     = request.POST.get('plot_land_status')
        address              = request.POST.get('address')

        facility_id          = request.POST.getlist('facility_id')


        month  = datetime.datetime.now().month
        day    = datetime.datetime.now().day
        if len(str(month)) == 1:
            month = "0"+str(month)
        if len(str(day)) == 1:
            day = "0"+str(day)
        prefix = str(datetime.datetime.now().year)+str(month)+str(day)
        if get_last:
            plotland_id     = int(get_last.plotland_id)+1
        else:
            plotland_id     = prefix+"01"
        
  
        
        document_path = ""
        if bool(request.FILES.get('plot_land_image', False)) == True:
            file = request.FILES['plot_land_image']   
            if not os.path.exists("plot_land_image/"):
                os.mkdir("plot_land_image/")

            document_path = default_storage.save("plot_land_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("plot_land_image/")+str(document_path).split("/")[-1] 
        
       

        plotlandid = PlotLandEntry.objects.create(date=date,plotland_id=plotland_id,developer_name_id=developer_name,
        plot_land_image=document_path,
            block=block,google_map_url=map_url,sector=sector,road_no=road_no,plot_no=plot_no,land_size=land_size,
            measurement_scale_id=measurement_scale,plot_land_status_id=plot_land_status,address=address,
            created_by_id=int(request.session['userid'])
        )
        for facility_id in facility_id:
            PlotLandFacility.objects.create(plotland_id = plotlandid,land_facility_id=facility_id)

        

        messages.success(request, 'Plot Land has been saved successfully.')
        return redirect("/property/create-property/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,'getsclale':getsclale,
        'getlandstatus':getlandstatus,'landfacility':landfacility,
        'getplotproject':getplotproject,
    }
    return render(request,'property/dashboard/create-property.html',context)


def plotlandlist(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    getproperty        = PropertyEntry.objects.filter(status=1)
    getplot            = PlotLandEntry.objects.filter(status=1)

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getproperty':getproperty,
        'getplot':getplot,
    }

    return render(request,'property/dashboard/plot-land-list.html',context)

def plotland_edit(request,plotland_id):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    getsclale          = MeasurementScale.objects.filter(status=1)
    getlandstatus      = PlotLandStatus.objects.filter(status=1)
    landfacility       = LandFacilityEntry.objects.all()
    getplotproject     = ProjectPlotLand.objects.all()
    getplot            = PlotLandEntry.objects.get(plotland_id=plotland_id)
    getplot_facility   = PlotLandFacility.objects.filter(plotland_id=plotland_id)

    print("data", landfacility)


    if request.method=="POST":
        developer_name       = request.POST.get('developer_name')
        block                = request.POST.get('block')
        google_map_url       = request.POST.get('google_map_url')
        sector               = request.POST.get('sector')
        road_no              = request.POST.get('road_no')
        plot_no              = request.POST.get('plot_no')
        land_size            = request.POST.get('land_size')
        measurement_scale    = request.POST.get('measurement_scale')
        plot_land_status     = request.POST.get('plot_land_status')
        address              = request.POST.get('address')

        facility_id          = request.POST.getlist('facility_id')


   
        
  
        plot_land_image = str(getplot.plot_land_image) if getplot.plot_land_image else ""
        if bool(request.FILES.get('plot_land_image', False)) == True: 
            if os.path.exists(str(plot_land_image)):
                os.remove(str(getplot.plot_land_image))

            file = request.FILES['plot_land_image']
            plot_land_image = "plot_land_image/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/plot_land_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/plot_land_image/') 
            plot_land_image = default_storage.save("plot_land_image/"+file.name, ContentFile(file.read())) 
            if plot_land_image:
                plot_land_image = str("plot_land_image/")+str(plot_land_image).split("/")[-1]


        
       

        PlotLandEntry.objects.filter(plotland_id=plotland_id).update(developer_name_id=developer_name,
            plot_land_image=plot_land_image,
            block=block,google_map_url=google_map_url,sector=sector,road_no=road_no,plot_no=plot_no,land_size=land_size,
            measurement_scale_id=measurement_scale,plot_land_status_id=plot_land_status,address=address,
            created_by_id=int(request.session['userid'])
        )

        for facility_id in facility_id:
            PlotLandFacility.objects.filter(plotland_id=plotland_id).update(land_facility_id=facility_id)

        

        messages.success(request, 'Plot Land has been updated successfully.')
        return redirect("/property/plot-land-list/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,'getsclale':getsclale,
        'getlandstatus':getlandstatus,'landfacility':landfacility,
        'getplotproject':getplotproject,
        'getplot':getplot,'getplot_facility':getplot_facility,
    }
    return render(request,'property/dashboard/plot-land-edit.html',context)

def plotland_delete(request,plotland_id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    PlotLandEntry.objects.filter(plotland_id=plotland_id).delete()
    messages.success(request, 'Plot / Land has been deleted successfully.')
    return redirect("/property/plot-land-list/")

def projectproperty(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    projecttype        = PropertyType.objects.filter(status=1)
   

    if request.method=="POST":
        project_name         = request.POST.get('project_name')
        developer_name       = request.POST.get('developer_name')
        address              = request.POST.get('address')
        project_type         = request.POST.get('project_type')
        total_apartment      = request.POST.get('total_apartment')
        land_size            = request.POST.get('land_size')
        total_units          = request.POST.get('total_units')
        lift                 = request.POST.get('lift')
        stairs               = request.POST.get('stairs')
        face                 = request.POST.get('face')
        plot_no              = request.POST.get('plot_no')
        block_no             = request.POST.get('block_no')
        road_size            = request.POST.get('road_size')
        parking_ability      = request.POST.get('parking_ability')

        document_path = ""
        if bool(request.FILES.get('project_logo', False)) == True:
            file = request.FILES['project_logo']   
            if not os.path.exists("logo/"):
                os.mkdir("logo/")

            document_path = default_storage.save("logo/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("logo/")+str(document_path).split("/")[-1] 
        
        

        ProjectAdd.objects.create(project_name=project_name,project_logo=document_path,developer_name=developer_name,
            address=address,project_type_id=project_type,total_apartment=total_apartment,land_size=land_size,
            total_units=total_units,lift=lift,stairs=stairs,face=face,plot_no=plot_no,block_no=block_no,
            road_size=road_size,parking_ability=parking_ability,
            created_by_id=int(request.session['userid'])
        )


        messages.success(request, 'Property project has been saved successfully.')
        return redirect("/property/project-add/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'projecttype':projecttype,
    }
    return render(request,'property/dashboard/create-project.html',context)


def property_project_edit(request,id):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    projecttype        = PropertyType.objects.filter(status=1)
    get_property_project  = ProjectAdd.objects.get(id=id)
   

    if request.method=="POST":
        project_name         = request.POST.get('project_name')
        developer_name       = request.POST.get('developer_name')
        address              = request.POST.get('address')
        project_type         = request.POST.get('project_type')
        total_apartment      = request.POST.get('total_apartment')
        land_size            = request.POST.get('land_size')
        total_units          = request.POST.get('total_units')
        lift                 = request.POST.get('lift')
        stairs               = request.POST.get('stairs')
        face                 = request.POST.get('face')
        plot_no              = request.POST.get('plot_no')
        block_no             = request.POST.get('block_no')
        road_size            = request.POST.get('road_size')
        parking_ability      = request.POST.get('parking_ability')

        
        project_logo = str(get_property_project.project_logo) if get_property_project.project_logo else ""
        if bool(request.FILES.get('project_logo', False)) == True: 
            if os.path.exists(str(project_logo)):
                os.remove(str(get_property_project.project_logo))

            file = request.FILES['project_logo']
            project_logo = "logo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/logo/'):
                os.mkdir('realstateapp/static/realstateapp/media/logo/') 
            project_logo = default_storage.save("logo/"+file.name, ContentFile(file.read())) 
            if project_logo:
                project_logo = str("logo/")+str(project_logo).split("/")[-1] 
        
        

        ProjectAdd.objects.filter(id=id).update(project_name=project_name,project_logo=project_logo,developer_name=developer_name,
            address=address,project_type_id=project_type,total_apartment=total_apartment,land_size=land_size,
            total_units=total_units,lift=lift,stairs=stairs,face=face,plot_no=plot_no,block_no=block_no,
            road_size=road_size,parking_ability=parking_ability,
            created_by_id=int(request.session['userid'])
        )


        messages.success(request, 'Property project has been updated successfully.')
        return redirect("/property/property-project/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'projecttype':projecttype,
        'get_property_project':get_property_project,
    }
    return render(request,'property/dashboard/property-project-edit.html',context)


def property_project_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    ProjectAdd.objects.filter(id=id).delete()
    messages.success(request, 'Property project has been deleted successfully.')
    return redirect("/faq-list/")


def propertyprojectlist(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    getpropertyproject = ProjectAdd.objects.filter(status=1)
   

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getpropertyproject':getpropertyproject,
    }
    return render(request,'property/dashboard/property-project-list.html',context)


def projectplotland(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    projecttype        = PropertyType.objects.filter(status=1)
   

    if request.method=="POST":
        block         = request.POST.get('block')
        sector        = request.POST.get('sector')
        road_no              = request.POST.get('road_no')
        plot_no         = request.POST.get('plot_no')
        land_size      = request.POST.get('land_size')
        size_unit      = request.POST.get('size_unit')
        developer_name      = request.POST.get('developer_name')
        map_url      = request.POST.get('map_url')
        address      = request.POST.get('address')

        

        document_path = ""
        if bool(request.FILES.get('plot_land_image', False)) == True:
            file = request.FILES['plot_land_image']   
            if not os.path.exists("plot_land_image/"):
                os.mkdir("plot_land_image/")

            document_path = default_storage.save("plot_land_image/"+file.name, ContentFile(file.read()))
            if document_path:
                document_path = str("plot_land_image/")+str(document_path).split("/")[-1] 
        
        

        ProjectPlotLand.objects.create(block=block,sector=sector,road_no=road_no,
            plot_no=plot_no,land_size=land_size,size_unit=size_unit,developer_name=developer_name,
            map_url=map_url,address=address,plot_land_image=document_path,
            created_by_id=int(request.session['userid'])
        )


        messages.success(request, 'plot/land project has been saved successfully.')
        return redirect("/property/project-add/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'projecttype':projecttype,
    }
    return render(request,'property/dashboard/create-project.html',context)




def land_project_edit(request,id):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    projecttype        = PropertyType.objects.filter(status=1)
    get_land           = ProjectPlotLand.objects.get(id=id)
   

    if request.method=="POST":
        block         = request.POST.get('block')
        sector        = request.POST.get('sector')
        road_no              = request.POST.get('road_no')
        plot_no         = request.POST.get('plot_no')
        land_size      = request.POST.get('land_size')
        size_unit      = request.POST.get('size_unit')
        developer_name      = request.POST.get('developer_name')
        map_url      = request.POST.get('map_url')
        address      = request.POST.get('address')

        plot_land_image = str(get_land.plot_land_image) if get_land.plot_land_image else ""
        if bool(request.FILES.get('plot_land_image', False)) == True: 
            if os.path.exists(str(plot_land_image)):
                os.remove(str(get_land.plot_land_image))

            file = request.FILES['plot_land_image']
            plot_land_image = "logo/"+file.name 
            if not os.path.exists('realstateapp/static/realstateapp/media/plot_land_image/'):
                os.mkdir('realstateapp/static/realstateapp/media/plot_land_image/') 
            plot_land_image = default_storage.save("plot_land_image/"+file.name, ContentFile(file.read())) 
            if plot_land_image:
                plot_land_image = str("plot_land_image/")+str(plot_land_image).split("/")[-1] 

        ProjectPlotLand.objects.filter(id=id).update(block=block,sector=sector,road_no=road_no,
            plot_no=plot_no,land_size=land_size,size_unit=size_unit,developer_name=developer_name,
            map_url=map_url,address=address,plot_land_image=plot_land_image,
            created_by_id=int(request.session['userid'])
        )


        messages.success(request, 'plot/land project has been updated successfully.')
        return redirect("/property/land-project/")

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'projecttype':projecttype,
        'get_land':get_land,
    }
    return render(request,'property/dashboard/land-project-edit.html',context)




def landprojectlist(request):
    user               = UserRegistrations.objects.get(id=int(request.session['userid']),status=1)
    comprofile         = CompanyProfile.objects.all().first()
    getprofile         = CompanyProfile.objects.filter(status=1)
    getplotland        = ProjectPlotLand.objects.filter(status=1)
   

    context={
        'user':user,
        'get_profile':comprofile,
        'getprofile':getprofile,
        'getplotland':getplotland,
    }
    return render(request,'property/dashboard/land-project-list.html',context)


def land_project_delete(request,id):
    if request.session.get('userid') == False:
        return redirect('/dashboard-login/')
    ProjectPlotLand.objects.filter(id=id).delete()
    messages.success(request, 'land project has been deleted successfully.')
    return redirect("/property/land-project/")