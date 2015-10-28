# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_transfer_plan',
            name='duration',
            field=durationfield.db.models.fields.duration.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='data_transfer_plan',
            name='freq',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
