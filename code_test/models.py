from django.db import models

# Create your models here.


class Kid(models.Model):

    first_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
