# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20151226_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='follow_up_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
