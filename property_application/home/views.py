from django.shortcuts import render
from django.http import JsonResponse


from .models import MasterState , PropertyType, CityMaster , Location, ReferenceMaster ,Details


def Home(request):
    if(request.method == 'POST'):
        
        name = request.POST.get('name')
        number = request.POST.get('number')
        property_type = request.POST.get('property')
        city = request.POST.get('city')
        location = request.POST.get('location')
        remark = request.POST.get('description')
        reference = request.POST.get('ref')
        state = request.POST.get('state')

        data  = Details.objects.create(
            name = name,
            number = number ,
            state_id = state ,
            city_id = city,
            location_id = location ,
            propertyType_id = property_type,
            referenceType_id = reference,
            remark = remark ,
            customerType_id = 1 
        )
        data.save()
        

        
    return render(request,'D://Property_web//property_application//templates//real_estate//index.html')

def New(request):
    return render(request,'D://Property_web//property_application//templates//real_estate//new.html')


def Property_List(request):
    return render(request,'D://Property_web//property_application//templates//real_estate//product_list.html')


def ContactPage(request):
    return render(request,'D://Property_web//property_application//templates//real_estate//contact_new.html')

def Contact(request):
    return render(request,'D://Property_web//property_application//templates//real_estate//contact.html')

def DetailForm(request):

    stateList  = MasterState.objects.filter(is_active = True)
    propertyTypeList =  PropertyType.objects.filter(is_active = True)
    ref_list = ReferenceMaster.objects.filter(is_active = True)

    if(request.method == 'POST'):
        print("hit the submit button")
        name = request.POST.get('name')
        number = request.POST.get('number')

        print("name = ",name)

    context = {
        'stateList' : stateList,
        'propertyTypeList' : propertyTypeList,
        'ref_list' : ref_list
    }

    return render(request,'D://Property_web//property_application//templates//real_estate//detail_form.html',context)



def get_cities_by_state(request):
    state_id = request.GET.get('state_id')
    cities = CityMaster.objects.filter(state_id=state_id, is_active=True)
    city_list = list(cities.values('city_id', 'city_name'))
    return JsonResponse({'cities': city_list})

def get_location_by_city(request):
    city_id = request.GET.get('city_id')
    locations = Location.objects.filter(city_id = city_id, is_active  = True)
    location_list = list(locations.values('location_id','location_name'))
    return JsonResponse({'locations' : location_list})
