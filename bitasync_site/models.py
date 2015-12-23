from django.db import models
from durationfield.db.models.fields.duration import DurationField
import datetime

from django.contrib.auth.models import User

class Data_Transfer_Plan(models.Model):

    plan_name = models.CharField(max_length=10)
    freq = models.IntegerField(default=0, null=True, blank=True)
    duration = DurationField(null=True, blank=True)
    description = models.CharField(max_length=1000, default="data plan description")
    long_description = models.CharField(max_length=1000, default="long description for a data transfer plan")
    price = models.IntegerField(default = 0)
    
    
    def __unicode__(self): 
        return self.plan_name

class Contact_Comment(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1000)
    call_back_request = models.NullBooleanField(null=True,blank=True)
    phone_number= models.CharField(null=True,blank=True,max_length=20)

class B2C_Coupon:
    pass


class B2S2C_Coupon:
    pass
    

    

