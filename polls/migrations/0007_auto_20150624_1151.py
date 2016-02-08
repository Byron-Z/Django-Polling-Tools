# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150624_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='appname',
            field=models.CharField(max_length=128),
        ),
    ]
