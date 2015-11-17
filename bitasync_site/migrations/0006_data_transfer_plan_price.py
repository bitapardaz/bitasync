# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0005_data_transfer_plan_descriptoin'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_transfer_plan',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
