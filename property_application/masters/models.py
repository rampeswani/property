from django.db import models

# Create your models here.


class BHK(models.Model):
    bhk_id = models.AutoField(primary_key= True)
    bhk_name = models.IntegerField()
    is_active = models.BooleanField(default= True)

    

    def __str__(self):
        return str(self.bhk_name )

    class Meta :
        ordering = ['bhk_id']