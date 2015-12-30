# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkLicenseManagement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_index', models.BigIntegerField(default=0)),
                ('bulk_license_username_prefix', models.CharField(default=b'gooshi', max_length=20)),
            ],
        ),
    ]
