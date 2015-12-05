# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0012_purchase_follow_up_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_transfer_plan',
            name='long_description',
            field=models.CharField(default=b'long description for a data transfer plan', max_length=1000),
        ),
    ]
