from django.shortcuts import render
from home.models import MasterState
from masters.models import BHK
from .models import PropertList
import uuid
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from django.core.paginator import Paginator

cloudinary.config( 
    cloud_name = "dqz4xasg5", 
    api_key = "969749835419172", 
    api_secret = "a5v1GiUa5cPZDpOLAdG3MIPAA-0", # Click 'View API Keys' above to copy your API secret
    secure=True
)


import os 
from django.conf import settings

# Create your views here.
def PropertyList(request):
    paginator = Paginator(properties, 4)  # Show 4 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("Total Properties:", properties.count())
    print("Current Page:", page_obj.number if page_obj else "None")

    context = {
        'page_obj' : page_obj
    }
    return render(request,'property-listing/property_list.html',context)


def PropertyAdd(request):
    stateList = MasterState.objects.all()
    bhkList = BHK.objects.all()

    if request.method=="POST":
        title = request.POST.get('title')
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        remark = request.POST.get('remark')
        bhk = request.POST.get('bhk')
        parking = request.POST.get('parking')
        bathroom =request.POST.get('bathroom')
        balcony = request.POST.get('balcony')

        sqrt_start = request.POST.get('sqrt_start')
        sqrt_end = request.POST.get('sqrt_end')

        price_start = request.POST.get('price_start')
        price_end = request.POST.get('price_end')

        photos = request.FILES.getlist('photo',None)
        

        property_create = PropertList.objects.create(
            property_list_title = title,
            state_id = state ,
            city_id = city,
            location_id = location,
            property_detail_remark = remark,
            property_sqrt_start_range = sqrt_start,
            property_sqrt_end_range = sqrt_end,

            property_price_start_range = price_start,
            property_price_end_range = price_end,

            bhk_id = bhk ,
            property_bathroom= bathroom,
            property_parking = parking,
            property_kitchne = balcony,

            created_by_id = request.session.get('user_id')
            
        )
        if photos:  # Ensure files were uploaded
            uploaded_urls = []  # Store all image URLs
            
            for file in photos:
                # Upload file to Cloudinary
                response = cloudinary.uploader.upload(file, folder=f"property_{property_create.property_list_id}")
                
                # Get the Cloudinary URL
                file_url = response.get('secure_url', '')  # Get secure URL
                
                if file_url:
                    uploaded_urls.append(file_url)

            # Store the first uploaded image URL (you can modify this for multiple images)
            if uploaded_urls:
                property_create.file_url = uploaded_urls[0]  # Save the first image
                property_create.save()

        


    context = {
        'stateList' : stateList ,
        'bhkList' : bhkList
    }
    return render(request,'property-listing/property_create.html',context)

def PropertyListWeb(request):
    keyword = request.GET.get('keyword', '')  # Get keyword from GET request

    print("keyword = ",keyword)
    data = PropertList.objects.all()
    paginator = Paginator(data, 4)  # Show 4 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print("Current Page:", page_obj.number if page_obj else "None")

    
    context={
        'data' : data,
        'page_obj' : page_obj

    }
    return render(request,'property-listing/property_list_web.html',context)


def partial(request):
    data = PropertList.objects.all()
    keyword = request.GET.get('keyword', '').strip()  # Get keyword from GET request

    print("keyword = ",keyword)
    if keyword:
        data = data.filter(property_list_title__icontains=keyword) 
    paginator = Paginator(data, 4)  # Show 4 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print("Current Page:", page_obj.number if page_obj else "None")

    
    context={
        'data' : data,
        'page_obj' : page_obj

    }
    return render(request,'property-listing/partial_pages/_load_property_list_data_web.html',context)
