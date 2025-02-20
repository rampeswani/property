from django.db import models
from home.models import Location ,CityMaster,MasterState
from django.contrib.auth.models import User, Group
from masters.models import BHK
import os 
# Create your models here.

class PropertList(models.Model):
    property_list_id = models.AutoField(primary_key = True)
    property_list_title = models.CharField(max_length = 100)
    state = models.ForeignKey(MasterState,related_name='PropertyList_MasterState', on_delete=models.CASCADE)
    city = models.ForeignKey(CityMaster,related_name = "PropertyList_CityMaster", on_delete = models.CASCADE)
    location = models.ForeignKey(Location, related_name = "PropertyList_Location", on_delete=models.CASCADE)
    bhk = models.ForeignKey(BHK,related_name = 'PropertList_BHK' , on_delete=models.CASCADE)

    property_detail_remark = models.TextField()
    
    property_sqrt_start_range = models.DecimalField(decimal_places=2, max_digits=10)
    property_sqrt_end_range = models.DecimalField(decimal_places=2, max_digits=10)
    #price 
    property_price_start_range = models.DecimalField(decimal_places=2, max_digits=10)
    property_price_end_range = models.DecimalField(decimal_places=2, max_digits=10)

    property_bathroom = models.IntegerField()
    property_kitchne = models.IntegerField()
    property_parking = models.IntegerField()

    file_url = models.CharField(max_length=1000,null = True,blank = True)
    file_url_2 = models.CharField(max_length=1000,null = True, blank = True)




    
    
    created_by = models.ForeignKey(User, related_name ='PropertyList_created_by' , on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,related_name='PropertyList_updated_by', on_delete=models.CASCADE, null = True, blank = True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.property_list_title

    class Meta :
        ordering = ['property_list_id']
