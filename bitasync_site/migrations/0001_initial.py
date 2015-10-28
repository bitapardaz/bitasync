# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Transfer_Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_name', models.CharField(max_length=10)),
                ('duration', models.DurationField(null=True)),
                ('frequency', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
