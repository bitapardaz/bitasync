# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20151108_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='B2C_Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Expiery_data', models.DateField()),
                ('Discount_rate', models.FloatField(default=0.0)),
                ('hashcode', models.CharField(max_length=50)),
                ('customer_profile', models.ForeignKey(blank=True, to='user_profile.CustomerProfile', null=True)),
            ],
        ),
    ]
