# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_logstring_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='appname',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipaddr',
            field=models.CharField(unique=True, max_length=16),
        ),
    ]
