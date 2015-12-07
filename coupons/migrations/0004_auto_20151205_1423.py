# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_auto_20151130_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='hashcode',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
