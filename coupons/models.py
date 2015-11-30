from django.db import models
from django.db.models import signals
from utilities import utility_functions
from user_profile.models import CustomerProfile
from .signals import b2c_coupon_created

# Create your models here.
class B2C_Coupon(models.Model):

    Expiery_data = models.DateField()
    Discount_rate = models.FloatField(default=0.0)
    hashcode = models.CharField(max_length=50,editable=False)

    customer_profile = models.ForeignKey(CustomerProfile, blank=True, null=True)
    
signals.post_save.connect(b2c_coupon_created, sender=B2C_Coupon, weak=False)
    