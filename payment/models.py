from django.db import models
from django.contrib.auth.models import User
from bitasync_site.models import Data_Transfer_Plan

class Purchase(models.Model):

    user = models.ForeignKey(User, related_name='customer')
    data_transfer_plan = models.ForeignKey(Data_Transfer_Plan)
    # to do. store agents' name in the database, and give her some rewards.
    # this can be used in the admin interface that we design for our customer
    # service team.
    # assisting_agent = models.ForeignKey(Sales_Agent)

    purchase_date = models.DateField(auto_now_add=True)
    amount_paid = models.FloatField(default=0)
    follow_up_number = models.CharField(max_length=100, null=True, blank=True)

    # access control.
    remaining_allowance_frequency = models.IntegerField(default=0)

    # managing purchase records that are associated with
    # shops selling a post-paid license
    shop_debited = models.BooleanField(default=False)
    # we store the shop entitiy related to the shop
    selling_shop = models.ForeignKey(User, blank=True, null=True,
                                     related_name='selling_shop')

    gateway = models.CharField(max_length=100, null=True,
                               blank=True, default="unspecified")
