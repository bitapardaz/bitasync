# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bitasync_site', '0014_auto_20151223_1452'),
        ('payment', '0004_auto_20151230_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingPurchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashcode', models.CharField(max_length=50, null=True, blank=True)),
                ('time_created', models.DateField(auto_now_add=True)),
                ('data_transfer_plan', models.ForeignKey(to='bitasync_site.Data_Transfer_Plan')),
                ('user', models.ForeignKey(related_name='end_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
