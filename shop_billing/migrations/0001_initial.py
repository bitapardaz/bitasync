# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0014_auto_20151223_1452'),
        ('user_profile', '0003_auto_20151226_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agreed_price', models.FloatField(default=0)),
                ('data_transfer_plan', models.ForeignKey(to='bitasync_site.Data_Transfer_Plan')),
                ('shop_profile', models.ForeignKey(to='user_profile.ShopProfile')),
            ],
        ),
    ]
