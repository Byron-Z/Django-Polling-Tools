# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_log_rollback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
            ],
            options={
                'verbose_name': 'Search',
                'proxy': True,
                'verbose_name_plural': 'Search',
            },
            bases=('polls.application',),
        ),
    ]
