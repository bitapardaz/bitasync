# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitasync_site', '0003_contact_us_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_US_Comment',
            new_name='Contact_Comment',
        ),
    ]
