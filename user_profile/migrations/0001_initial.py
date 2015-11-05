# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_mobile', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('bank_card_number', models.CharField(max_length=20, null=True, blank=True)),
                ('bank_card_holder', models.CharField(max_length=30, null=True, blank=True)),
                ('rewared', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_shop', models.BooleanField()),
                ('email_subscription', models.BooleanField(default=True)),
                ('mobile', models.CharField(max_length=20, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='user_profile',
            field=models.OneToOneField(to='user_profile.UserProfile'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user_profile',
            field=models.OneToOneField(to='user_profile.UserProfile'),
        ),
    ]
