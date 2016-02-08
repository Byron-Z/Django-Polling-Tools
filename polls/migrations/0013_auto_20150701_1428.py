# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20150629_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='path',
            field=models.CharField(max_length=512, validators=[polls.models.validate_path]),
        ),
    ]
