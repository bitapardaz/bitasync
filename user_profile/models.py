from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_shop = models.BooleanField()
    email_subscription = models.BooleanField(default=True)
    mobile = models.CharField(null=True,blank=True, max_length=20)    
    
class ShopProfile(models.Model):

    user_profile = models.OneToOneField(UserProfile)  
    address = models.CharField(null=True, blank=True, max_length=100)
    landline = models.CharField(null=True, blank=True, max_length=20)
    bank_card_number = models.CharField(null=True,blank=True, max_length=20)
    account_holder = models.CharField(null=True,blank=True, max_length=30)
    reward = models.BigIntegerField(default=0)    
    
class CustomerProfile(models.Model):
    
    user_profile = models.OneToOneField(UserProfile)    
    latest_mobile = models.CharField(null=True,blank=True,max_length=30)     

