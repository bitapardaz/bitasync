# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20151108_1833'),
        ('coupons', '0002_auto_20151130_1242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='B2C_Coupon',
            new_name='Coupon',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='customer_profile',
        ),
        migrations.AddField(
            model_name='coupon',
            name='user_profile',
            field=models.ForeignKey(blank=True, to='user_profile.UserProfile', null=True),
        ),
    ]
