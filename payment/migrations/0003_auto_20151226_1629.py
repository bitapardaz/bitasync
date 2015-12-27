# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_purchase_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='remaining_allowance_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='selling_shop',
            field=models.ForeignKey(related_name='selling_shop', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='shop_debited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
