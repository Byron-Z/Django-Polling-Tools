# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(unique=True, max_length=64, validators=[polls.models.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipaddr',
            field=models.CharField(unique=True, max_length=16, validators=[django.core.validators.validate_ipv46_address]),
        ),
    ]
