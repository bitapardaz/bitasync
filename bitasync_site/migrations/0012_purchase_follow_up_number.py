# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0011_auto_20151118_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='follow_up_number',
            field=models.CharField(default='unspecified', max_length=100),
            preserve_default=False,
        ),
    ]
