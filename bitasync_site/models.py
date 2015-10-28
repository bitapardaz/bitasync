from django.db import models
from durationfield.db.models.fields.duration import DurationField


class Data_Transfer_Plan(models.Model):

    plan_name = models.CharField(max_length=10)
    freq = models.IntegerField(default=0, null=True , blank=True)
    duration = DurationField(null=True , blank=True)

class B2C_Coupon
    pass


class B2S2C_Coupon
    pass
