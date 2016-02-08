# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_log_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='rollback',
        ),
    ]
