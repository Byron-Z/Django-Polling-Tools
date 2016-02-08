# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20150701_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='runningtime',
        ),
        migrations.RemoveField(
            model_name='process',
            name='runningtime',
        ),
    ]
