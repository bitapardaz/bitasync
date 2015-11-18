# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0008_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='gateway',
            field=models.CharField(default=b'unspecified', max_length=100, null=True, blank=True),
        ),
    ]
