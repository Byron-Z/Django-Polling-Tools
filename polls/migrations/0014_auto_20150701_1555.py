# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20150701_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='endtime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='starttime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='endtime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='starttime',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
