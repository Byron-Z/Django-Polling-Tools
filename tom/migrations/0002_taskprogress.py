# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskProgress',
            fields=[
            ],
            options={
                'verbose_name': 'TaskProgress',
                'proxy': True,
                'verbose_name_plural': 'TaskProgress',
            },
            bases=('tom.applications',),
        ),
    ]
