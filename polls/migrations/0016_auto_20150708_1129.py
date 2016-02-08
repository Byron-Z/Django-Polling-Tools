# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20150706_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='endtime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='monitortime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='starttime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='endtime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='monitortime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='severity',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='starttime',
            field=models.TimeField(null=True),
        ),
    ]
