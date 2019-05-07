# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
    ]
