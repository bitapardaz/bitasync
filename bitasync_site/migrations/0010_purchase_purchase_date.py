# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0009_purchase_gateway'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(default=datetime.datetime(2015, 11, 18, 13, 17, 2, 899641, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
