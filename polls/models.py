# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import validate_ipv46_address
from django.db.models.signals import pre_save
import re
import datetime



def validate_model(sender, **kwargs):
    if 'raw' in kwargs and not kwargs['raw']:
        kwargs['instance'].full_clean()
pre_save.connect(validate_model, dispatch_uid='validate_models')

def validate_hostname(hostname):
    if len(hostname) > 255:
        raise ValidationError("Enter a valid host name!")
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    if re.search(r'(?!-)[A-z\d-]{1,63}(?<!-)$', hostname) == None:
        raise ValidationError("Enter a valid host name!")


def validate_path(input_path):
    
    win = re.match(ur'^(?P<path>(?:[a-zA-Z]:)?\\(?:[^\\\?\/\*\|<>:"]+\\)+)(?P<filename>(?P<name>[^\\\?\/\*\|<>:"]+?)\.(?P<ext>[^.\\\?\/\*\|<>:"]+))$', input_path)
    unix = re.match('^(\/(?:[^\?\*\/\|<>:"]+\/?)*[^\/\|<>:&]+?)$', input_path)

    if (not win) and (not unix):
        raise ValidationError("Enter a valid Windows/Unix/Linux absolute path!")

class Application(models.Model):
    appid = models.AutoField(primary_key=True)
    appname = models.CharField(max_length=128, unique=True)
    manager = models.CharField(max_length=64)
    ownership = models.CharField(max_length=32)
    priority = models.CharField(max_length=16)
    developer = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'application'

class Search(Application):
    class Meta:
        proxy=True
        verbose_name = 'Search'
        verbose_name_plural = 'Search'

class Server(models.Model):
    sid = models.AutoField(primary_key=True)
    datacenter = models.CharField(max_length=16)
    hostname = models.CharField(max_length=64, unique=True, validators=[validate_hostname])
    ipaddr = models.CharField(max_length=16, unique=True, validators=[validate_ipv46_address])
    status = models.CharField(max_length=16)
    appid = models.ForeignKey(Application, db_column='appid')
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'server'


class Attachment(models.Model):
    attachid = models.IntegerField()
    uid = models.IntegerField(blank=True, null=True)
    uploadtime = models.DateTimeField(db_column='uploadTime', blank=True, null=True)  # Field name made lowercase.
    aname = models.CharField(max_length=255, blank=True, null=True)
    atype = models.CharField(max_length=255, blank=True, null=True)
    asize = models.CharField(max_length=20, blank=True, null=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    savepath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'attachment'


class Log(models.Model):
    lid = models.AutoField(primary_key=True)
    path = models.CharField(max_length=512, validators=[validate_path])
    sid = models.ManyToManyField('Server', db_column='sid')
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    monitortime = models.IntegerField(null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log'


class Logstring(models.Model):
    lsid = models.AutoField(primary_key=True)
    lid = models.ForeignKey(Log, db_column='lid')
    keywords = models.CharField(max_length=512)
    severity = models.CharField(max_length=16)

    class Meta:
        db_table = 'logstring'


class Process(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=128)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    monitortime = models.IntegerField(null=True)
    severity = models.CharField(max_length=16, null=True)
    sid = models.ManyToManyField('Server', db_column='sid')
    instance = models.IntegerField()
    keywords = models.CharField(max_length=512)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'process'

class Severity(models.Model):
    ssid = models.AutoField(primary_key=True)
    severity = models.CharField(max_length=16)

    class Meta:
        db_table = 'Severity'
