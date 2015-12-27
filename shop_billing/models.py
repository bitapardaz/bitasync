from django.db import models

from user_profile.models import ShopProfile
from bitasync_site.models import Data_Transfer_Plan


class RetailFee(models.Model):
    shop_profile = models.ForeignKey(ShopProfile)
    data_transfer_plan = models.ForeignKey(Data_Transfer_Plan)

    # the price that we agree  with  a shop on a given data transfer plan
    agreed_price = models.FloatField(default=0)
