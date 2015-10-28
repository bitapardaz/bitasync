# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Transfer_Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_name', models.CharField(max_length=10)),
                ('freq', models.IntegerField(default=0, null=True)),
                ('duration', durationfield.db.models.fields.duration.DurationField(null=True)),
            ],
        ),
    ]
