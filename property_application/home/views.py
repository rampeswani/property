from django.shortcuts import render
from django.http import JsonResponse
from .models import Details
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import MasterState , PropertyType, CityMaster , Location, ReferenceMaster ,Details,CustomerType
from django.contrib.auth.decorators import login_required

# def Home(request):
#     if(request.method == 'POST'):
#         print("inside the post of home view detail form")
        
#         name = request.POST.get('name')
#         number = request.POST.get('number')
#         property_type = request.POST.get('property')
#         city = request.POST.get('city')
#         location = request.POST.get('location')
#         remark = request.POST.get('description')
#         reference = request.POST.get('ref')
#         state = request.POST.get('state')
#         customer_type = request.POST.get('')

#         data  = Details.objects.create(
#             name = name,
#             number = number ,
#             state_id = state ,
#             city_id = city,
#             location_id = location ,
#             propertyType_id = property_type,
#             referenceType_id = reference,
#             remark = remark ,
#             customerType_id = 1 
#         )
#         data.save()
#         #print("printing the user id ",request.user_id)
        

        
#     return render(request,'real_estate/home.html')
from propertyListing.models import PropertList
from django.core.paginator import Paginator
from django.shortcuts import redirect
def Home(request):
    if(request.method == 'POST'):
        print("inside the post of home view detail form")
        
        name = request.POST.get('name')
        number = request.POST.get('number')
        property_type = request.POST.get('property')
        city = request.POST.get('city')
        location = request.POST.get('location')
        remark = request.POST.get('description')
        reference = request.POST.get('ref')
        state = request.POST.get('state')
        customer_type = request.POST.get('')

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
        #print("printing the user id ",request.user_id)
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

def New(request):
    
    return render(request,'real_estate//new.html')


def Property_List(request):
    return render(request,'real_estate//product_list.html')


def ContactPage(request):
    print("hello")
    print("printing the user id ",request.session.get('user_id'))
    return render(request,'real_estate//contact_new.html')

def Contact(request):
    print("hello")
    # print("printing the user id ",request.user_id)
    
    return render(request,'real_estate//contact.html')

def DetailForm(request):

    stateList  = MasterState.objects.filter(is_active = True)
    propertyTypeList =  PropertyType.objects.filter(is_active = True)
    ref_list = ReferenceMaster.objects.filter(is_active = True)
    customerTypeList = CustomerType.objects.all()

    if(request.method == 'POST'):
        print("hit the submit button")
        name = request.POST.get('name')
        number = request.POST.get('number')

        print("name = ",name)

    context = {
        'stateList' : stateList,
        'propertyTypeList' : propertyTypeList,
        'ref_list' : ref_list,
        'customerTypeList' : customerTypeList
    }

    return render(request,'real_estate/detail_form.html',context)



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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def Login(request):
    if request.method == 'POST':
        print("inside login method")
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id  # Store user ID in session
            request.session['username'] = user.username  # Store username in session
            return redirect("admin")  # Redirect to a dashboard or home page
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login/login.html")



def Logout(request):
    logout(request)  # Logs out the user
    request.session.flush()  # Clears all session data
    return redirect("login")  # Redirect to the login page
    
@login_required
def admin(request):
    return render(request,'login/admin_index.html')



@login_required
def ListFormData(request):

    data = Details.objects.all()
    context = {
        'data' : data 
    }
    return render(request,'login/form_list.html',context)

def Big(request):
    return render(request,'real_estate/big_index.html')

from twilio.rest import Client
from django.conf import settings


def send_whatsapp_message(to,message):
    client=Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
    try :
        message=client.messages.create(
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=to
        )
        return f"message sent success  message sid :{message.sid}"
    except Exception  as e :
        return f"error {str(e)}"
    
def send_whatsapp(request):
    to = request.GET.get('to', 'whatsapp:+919893780766')  # Default number for testing
    message = request.GET.get('message', 'Hello from Django via WhatsApp!')
    
    response = send_whatsapp_message(to, message)
    
    return JsonResponse({"status": response})

def check(request):
    return render(request,'new/index.html')