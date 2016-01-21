from django.db import models

# Create your models here.
class KasperskyCounter(models.Model):
    clicks = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.clicks)
