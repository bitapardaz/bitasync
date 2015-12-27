# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20151108_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='debt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='shopprofile',
            name='reward',
            field=models.FloatField(default=0.0),
        ),
    ]
