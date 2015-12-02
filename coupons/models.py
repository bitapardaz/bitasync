from django.db import models
from django.db.models import signals
from utilities import utility_functions
from user_profile.models import UserProfile
from .signals import coupon_created

# Create your models here.
class Coupon(models.Model):

    expiry_date = models.DateField()
    discount_rate = models.FloatField(default=0.0)
    hashcode = models.CharField(max_length=50,editable=False)

    user_profile = models.ForeignKey(UserProfile, blank=True, null=True)
    
signals.post_save.connect(coupon_created, sender=Coupon, weak=False)
    
