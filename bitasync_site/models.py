from django.db import models

class Data_Transfer_Plan(models.Model):

    plan_name = models.CharField(max_length=10)
    duration = models.DurationField(null=True)
    frequency = models.IntegerField(default=0, null=True)
