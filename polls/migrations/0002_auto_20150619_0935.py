# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('ssid', models.AutoField(serialize=False, primary_key=True)),
                ('severity', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Severity',
            },
        ),
        migrations.RemoveField(
            model_name='log',
            name='instance',
        ),
        migrations.AlterField(
            model_name='log',
            name='endtime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='starttime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='endtime',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='starttime',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
