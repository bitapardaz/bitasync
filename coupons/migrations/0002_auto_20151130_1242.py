# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b2c_coupon',
            old_name='Discount_rate',
            new_name='discount_rate',
        ),
        migrations.RenameField(
            model_name='b2c_coupon',
            old_name='Expiery_data',
            new_name='expiry_date',
        ),
        migrations.AlterField(
            model_name='b2c_coupon',
            name='hashcode',
            field=models.CharField(max_length=50, editable=False),
        ),
    ]
