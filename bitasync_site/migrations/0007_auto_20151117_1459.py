# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0006_data_transfer_plan_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_transfer_plan',
            old_name='descriptoin',
            new_name='description',
        ),
    ]
