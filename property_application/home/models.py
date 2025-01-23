from django.db import models

# Create your models here.

class MasterState(models.Model) :
    state_id = models.AutoField(primary_key = True)
    state_name  = models.CharField(max_length= 100)
    is_active = models.BooleanField(default = True)

    
    def __str__(self):
        return self.state_name

    class Meta :
        ordering = ['state_id']


class CityMaster(models.Model):
    city_id = models.AutoField(primary_key= True)
    city_name = models.CharField(max_length=100)

    state= models.ForeignKey(MasterState, related_name='CityMaster_State', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (self.city_name)

    class Meta:
        ordering = ['city_id']

class Location(models.Model):
    location_id = models.AutoField(primary_key = True)
    location_name  = models.CharField(max_length = 150)
    city = models.ForeignKey(CityMaster , related_name ='Location_CityMaster', on_delete = models.CASCADE)

    
    is_active  = models.BooleanField(default = True)

    def __str__(self):
        return self.location_name
    
    class Meta :
        ordering = ['location_id']


class CustomerType(models.Model):
    type_id = models.AutoField(primary_key = True)
    type_name = models.CharField(max_length=100)

    is_active  = models.BooleanField(default=True)

    def __str__(self):
        return self.type_name

    class Meta :
        ordering = ['type_id']

class PropertyType(models.Model):
    property_type_id = models.AutoField(primary_key = True)
    property_type_name  = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.property_type_name

    class Meta:
        ordering = ['property_type_id']


class ReferenceMaster(models.Model):
    reference_id = models.AutoField(primary_key = True)
    reference_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.reference_name

    class Meta :
        ordering = ['reference_id']



# ---------------------Main Table ------- for details


class Details(models.Model):
    details_id = models.AutoField(primary_key = True)
    number = models.CharField(max_length=11)
    name  = models.CharField(max_length=200)
    email = models.EmailField(max_length=50 , null = True, blank=True) 
    remark = models.TextField(null=True, blank = True)

    state = models.ForeignKey(MasterState, related_name='Details_MasterState', on_delete=models.CASCADE)
    city = models.ForeignKey(CityMaster , related_name='Details_CityMaster', on_delete = models.CASCADE)
    location = models.ForeignKey(Location , related_name='Details_Location', on_delete=models.CASCADE)

    propertyType = models.ForeignKey(PropertyType , related_name='Details_PropertyType' , on_delete=models.CASCADE)
    referenceType = models.ForeignKey(ReferenceMaster , related_name='Details_ReferenceMaster' , on_delete=models.CASCADE)
    customerType = models.ForeignKey(CustomerType , related_name='Details_CustomerType' , on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

    class Meta :
        ordering = ['details_id']
