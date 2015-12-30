from django.db import models

from user_profile.models import ShopProfile
from bitasync_site.models import Data_Transfer_Plan


class RetailFee(models.Model):
    shop_profile = models.ForeignKey(ShopProfile)
    data_transfer_plan = models.ForeignKey(Data_Transfer_Plan)

    # the price that we agree  with  a shop on a given data transfer plan
    agreed_price = models.FloatField(default=0)

class BulkLicenseManagement(models.Model):
    current_index = models.BigIntegerField(default=0)
    bulk_license_username_prefix = models.CharField(default='gooshi',max_length=20)

    def __unicode__(self):
        return self.bulk_license_username_prefix + " --- " + str(self.current_index)
