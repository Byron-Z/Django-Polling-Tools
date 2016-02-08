# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('appid', models.AutoField(serialize=False, primary_key=True)),
                ('appname', models.CharField(max_length=128)),
                ('manager', models.CharField(max_length=64)),
                ('ownership', models.CharField(max_length=32)),
                ('priority', models.CharField(max_length=16)),
                ('developer', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attachid', models.IntegerField()),
                ('uid', models.IntegerField(null=True, blank=True)),
                ('uploadtime', models.DateTimeField(null=True, db_column='uploadTime', blank=True)),
                ('aname', models.CharField(max_length=255, null=True, blank=True)),
                ('atype', models.CharField(max_length=255, null=True, blank=True)),
                ('asize', models.CharField(max_length=20, null=True, blank=True)),
                ('extension', models.CharField(max_length=20, null=True, blank=True)),
                ('isdel', models.IntegerField(null=True, db_column='isDel', blank=True)),
                ('savepath', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'attachment',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('lid', models.AutoField(serialize=False, primary_key=True)),
                ('path', models.CharField(max_length=512)),
                ('runningtime', models.IntegerField(null=True, blank=True)),
                ('starttime', models.DateTimeField(null=True, blank=True)),
                ('endtime', models.DateTimeField(null=True, blank=True)),
                ('monitortime', models.IntegerField(null=True, blank=True)),
                ('rollback', models.IntegerField(null=True, blank=True)),
                ('instance', models.IntegerField()),
                ('remark', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'log',
            },
        ),
        migrations.CreateModel(
            name='Logstring',
            fields=[
                ('lsid', models.AutoField(serialize=False, primary_key=True)),
                ('keywords', models.CharField(max_length=512)),
                ('severity', models.CharField(max_length=16)),
                ('remark', models.TextField(null=True, blank=True)),
                ('lid', models.ForeignKey(to='polls.Log', db_column='lid')),
            ],
            options={
                'db_table': 'logstring',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('pname', models.CharField(max_length=128)),
                ('runningtime', models.IntegerField(null=True, blank=True)),
                ('starttime', models.DateTimeField(null=True, blank=True)),
                ('endtime', models.DateTimeField(null=True, blank=True)),
                ('monitortime', models.IntegerField(null=True, blank=True)),
                ('severity', models.CharField(max_length=16, null=True, blank=True)),
                ('instance', models.IntegerField()),
                ('keywords', models.CharField(max_length=512)),
                ('remark', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'process',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('sid', models.AutoField(serialize=False, primary_key=True)),
                ('datacenter', models.CharField(max_length=16)),
                ('hostname', models.CharField(max_length=64)),
                ('ipaddr', models.CharField(max_length=16)),
                ('status', models.CharField(max_length=16)),
                ('severity', models.CharField(max_length=16, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('appid', models.ForeignKey(to='polls.Application', db_column='appid')),
            ],
            options={
                'db_table': 'server',
            },
        ),
        migrations.AddField(
            model_name='process',
            name='sid',
            field=models.ForeignKey(to='polls.Server', db_column='sid'),
        ),
        migrations.AddField(
            model_name='log',
            name='pid',
            field=models.ForeignKey(to='polls.Process', db_column='pid'),
        ),
        migrations.AddField(
            model_name='log',
            name='sid',
            field=models.ForeignKey(to='polls.Server', db_column='sid'),
        ),
    ]
