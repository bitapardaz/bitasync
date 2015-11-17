from django.db import models
from durationfield.db.models.fields.duration import DurationField


class Data_Transfer_Plan(models.Model):

    plan_name = models.CharField(max_length=10)
    freq = models.IntegerField(default=0, null=True, blank=True)
    duration = DurationField(null=True, blank=True)
    description = models.CharField(max_length=1000, default="data plan description")
    price = models.IntegerField(default = 0)
    
    
    def __unicode__(self): 
        return self.plan_name

class Contact_Comment(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1000)

class B2C_Coupon:
    pass


class B2S2C_Coupon:
    pass
