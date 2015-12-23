# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0013_data_transfer_plan_long_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='data_transfer_plan',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
