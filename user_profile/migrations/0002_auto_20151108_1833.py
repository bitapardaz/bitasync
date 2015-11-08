# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopprofile',
            old_name='bank_card_holder',
            new_name='account_holder',
        ),
        migrations.RenameField(
            model_name='shopprofile',
            old_name='rewared',
            new_name='reward',
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='landline',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
