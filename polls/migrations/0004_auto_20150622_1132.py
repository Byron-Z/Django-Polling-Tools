# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_server_severity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='sid',
        ),
        migrations.AddField(
            model_name='log',
            name='sid',
            field=models.ManyToManyField(to='polls.Server', db_column='sid'),
        ),
        migrations.RemoveField(
            model_name='process',
            name='sid',
        ),
        migrations.AddField(
            model_name='process',
            name='sid',
            field=models.ManyToManyField(to='polls.Server', db_column='sid'),
        ),
    ]
