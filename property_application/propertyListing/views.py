from django.shortcuts import render
from home.models import MasterState
from masters.models import BHK
from .models import PropertList
import uuid

import os 
from django.conf import settings

# Create your views here.
def PropertyList(request):
    return render(request,'property-listing/property_list.html')


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

        photo = request.FILES.getlist('photo',None)
        

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
        if photo:  # Ensure files were uploaded
            for file in photo:  # Iterate over each uploaded file
                # Define folder path using property ID
                property_folder = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', f'property_{property_create.property_list_id}')
                os.makedirs(property_folder, exist_ok=True)  # Create the folder if it doesn't exist

                # Generate a unique filename
                unique_filename = str(uuid.uuid4()) + os.path.splitext(file.name)[1]  # UUID + extension
                file_path = os.path.join(property_folder, unique_filename)

                # Save file to static/uploads/property_{id}/
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                # Store relative path in the database (only saving the last uploaded file path)
                property_create.file_url = unique_filename
            
            # Save property object after all images are processed
            property_create.save()

        


    context = {
        'stateList' : stateList ,
        'bhkList' : bhkList
    }
    return render(request,'property-listing/property_create.html',context)