# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0014_auto_20151223_1452'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gateway', models.CharField(default=b'unspecified', max_length=100, null=True, blank=True)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('follow_up_number', models.CharField(max_length=100)),
                ('data_transfer_plan', models.ForeignKey(to='bitasync_site.Data_Transfer_Plan')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
