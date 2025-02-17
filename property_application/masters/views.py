from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
# from .models import Details
from django.contrib.auth import logout
from django.shortcuts import redirect
# from .models import MasterState , PropertyType, CityMaster , Location, ReferenceMaster ,Details
from django.contrib.auth.decorators import login_required
from .models import BHK
# Create your views here.

def BHKCreate(request):
    if request.method == "POST":
        print("inside master form")

        bhk = request.POST.get('bhk')

        data = BHK.objects.create(
            bhk_name = bhk 
        )
        data.save()
        return redirect('bhk-list')


    return render(request,'masters/bhk_create_form.html')

def BHKList(request):
    data = BHK.objects.filter(is_active= True)
    context = {
        'data' : data 
    }
    return render(request,'masters/bhk_list.html',context)


def MasterData(request):
    return render(request,'masters/master_data.html')