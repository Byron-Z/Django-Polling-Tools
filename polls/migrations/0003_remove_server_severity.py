# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150619_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='severity',
        ),
    ]
