from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from bitasync_site.models import Data_Transfer_Plan
from coupons.models import Coupon

class Purchase(models.Model):

    user = models.ForeignKey(User)
    data_transfer_plan = models.ForeignKey(Data_Transfer_Plan)           
    # to do. store agents' name in the database, and give her some rewards. 
    # this can be used in the admin interface that we design for our customer service team.  
    # assisting_agent = models.ForeignKey(Sales_Agent)
    
    gateway = models.CharField(max_length=100, null=True, blank=True, default="unspecified")
    purchase_date = models.DateField(auto_now_add=True )
    amount_paid = models.FloatField(default=0)
    follow_up_number = models.CharField(max_length=100)
    
    
    
    
