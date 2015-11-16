# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0004_auto_20151115_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_transfer_plan',
            name='descriptoin',
            field=models.CharField(default=b'data plan description', max_length=1000),
        ),
    ]
