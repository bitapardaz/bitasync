# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0010_purchase_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_comment',
            name='call_back_request',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='contact_comment',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
