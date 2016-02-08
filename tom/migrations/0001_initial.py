# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('appid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='AppID')),
                ('appname', models.CharField(max_length=255, null=True, db_column='AppName', blank=True)),
                ('appregistryid', models.CharField(max_length=15, null=True, db_column='AppRegistryID', blank=True)),
                ('appoperatingsystem', models.CharField(max_length=15, null=True, db_column='AppOperatingSystem', blank=True)),
                ('appownergroup', models.CharField(max_length=15, null=True, db_column='AppOwnerGroup', blank=True)),
                ('appoperationsuppgroup', models.CharField(max_length=15, null=True, db_column='AppOperationSuppGroup', blank=True)),
                ('appdeploysuppgroup', models.CharField(max_length=15, null=True, db_column='AppDeploySuppGroup', blank=True)),
                ('appdevmanager', models.CharField(max_length=15, db_column='AppDevManager')),
                ('appteamleadsupport', models.CharField(max_length=15, null=True, db_column='AppTeamLeadSupport', blank=True)),
                ('appteamleadtechops', models.CharField(max_length=15, null=True, db_column='AppTeamLeadTechOps', blank=True)),
                ('apptransitioncomplexity', models.CharField(max_length=15, null=True, db_column='AppTransitionComplexity', blank=True)),
                ('appclassregsci', models.CharField(max_length=15, null=True, db_column='AppClassRegSCI', blank=True)),
                ('appmarketedge', models.NullBooleanField(db_column='AppMarketEdge')),
                ('appcrossdatacenterdependencies', models.NullBooleanField(db_column='AppCrossDataCenterDependencies')),
                ('appsinglepointoffailure', models.NullBooleanField(db_column='AppSinglePointOfFailure')),
                ('appexternallyfacing', models.NullBooleanField(db_column='AppExternallyFacing')),
                ('appbehindwaf', models.NullBooleanField(db_column='AppBehindWAF')),
                ('applatencysensitive', models.NullBooleanField(db_column='AppLatencySensitive')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Applications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Classregscis',
            fields=[
                ('classregsci_id', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='ClassRegSCI_ID')),
                ('classregsci_desc', models.CharField(max_length=100, null=True, db_column='ClassRegSCI_Desc', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'ClassRegSCIs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Complexities',
            fields=[
                ('complexityid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='ComplexityID')),
                ('complexitydesc', models.CharField(max_length=100, null=True, db_column='ComplexityDesc', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Complexities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('componentid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='ComponentID')),
                ('componentname', models.CharField(max_length=100, db_column='ComponentName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Components',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contactid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='ContactID')),
                ('contactfirstname', models.CharField(max_length=100, null=True, db_column='ContactFirstName', blank=True)),
                ('contactlastname', models.CharField(max_length=100, null=True, db_column='ContactLastName', blank=True)),
                ('contactemail', models.CharField(max_length=255, null=True, db_column='ContactEmail', blank=True)),
                ('groupid', models.CharField(max_length=15, null=True, db_column='GroupID', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Contacts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datasources',
            fields=[
                ('datasourceid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='DataSourceID')),
                ('datasourcename', models.CharField(max_length=100, db_column='DataSourceName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'DataSources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Environments',
            fields=[
                ('environmentid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='EnvironmentID')),
                ('environmentname', models.CharField(max_length=100, db_column='EnvironmentName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Environments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('groupid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='GroupID')),
                ('groupname', models.CharField(max_length=100, null=True, db_column='GroupName', blank=True)),
                ('groupnasdaqdeptid', models.IntegerField(null=True, db_column='GroupNasdaqDeptID', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappcomponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppComponent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappdatasource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppDataSource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappenvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flaggedexempton', models.DateTimeField(null=True, db_column='FlaggedExemptOn', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppEnvironment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappmonitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppMonitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappnetworksegment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppNetworkSegment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappoperationwindow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppOperationWindow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Joinappproviderconsumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'JoinAppProviderConsumer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Milestones',
            fields=[
                ('milestoneid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='MilestoneID')),
                ('milestonedesc', models.CharField(max_length=100, null=True, db_column='MilestoneDesc', blank=True)),
                ('milestonerank', models.SmallIntegerField(null=True, db_column='MilestoneRank', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Milestones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('monitorid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='MonitorID')),
                ('monitorname', models.CharField(max_length=100, db_column='MonitorName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Monitors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Networksegments',
            fields=[
                ('networksegmentid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='NetworkSegmentID')),
                ('networksegmentname', models.CharField(max_length=100, db_column='NetworkSegmentName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'NetworkSegments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operatingsystems',
            fields=[
                ('operatingsystemid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='OperatingSystemID')),
                ('operatingsystemname', models.CharField(max_length=100, null=True, db_column='OperatingSystemName', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'OperatingSystems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operationwindows',
            fields=[
                ('operationwindowid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='OperationWindowID')),
                ('operationwindowname', models.CharField(max_length=100, db_column='OperationWindowName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'OperationWindows',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(serialize=False, primary_key=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('definition', models.BinaryField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taskgroups',
            fields=[
                ('taskgroupid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='TaskGroupID')),
                ('taskgroupname', models.CharField(max_length=100, db_column='TaskGroupName')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'TaskGroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('originaltargetdate', models.DateTimeField(null=True, db_column='OriginalTargetDate', blank=True)),
                ('currenttargetdate', models.DateTimeField(null=True, db_column='CurrentTargetDate', blank=True)),
                ('taskinprogress', models.BooleanField(db_column='TaskInProgress')),
                ('completionpercent', models.SmallIntegerField(db_column='CompletionPercent')),
                ('completiondate', models.DateTimeField(null=True, db_column='CompletionDate', blank=True)),
                ('tasknotes', models.TextField(null=True, db_column='TaskNotes', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.TextField(db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.TextField(db_column='UpdateBy')),
                ('flaggedexempton', models.DateTimeField(null=True, db_column='FlaggedExemptOn', blank=True)),
            ],
            options={
                'db_table': 'Tasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasktypes',
            fields=[
                ('tasktypeid', models.CharField(max_length=15, serialize=False, primary_key=True, db_column='TaskTypeID')),
                ('tasktypename', models.CharField(max_length=100, null=True, db_column='TaskTypeName', blank=True)),
                ('taskrank', models.SmallIntegerField(null=True, db_column='TaskRank', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'TaskTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('appid', models.ForeignKey(primary_key=True, db_column='AppID', serialize=False, to='tom.Applications', unique=True)),
                ('apppriority', models.SmallIntegerField(null=True, db_column='AppPriority', blank=True)),
                ('lastreviewdate', models.DateTimeField(null=True, db_column='LastReviewDate', blank=True)),
                ('lastreviewby', models.CharField(max_length=15, null=True, db_column='LastReviewBy', blank=True)),
                ('projectnotes', models.TextField(null=True, db_column='ProjectNotes', blank=True)),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('createby', models.CharField(max_length=50, db_column='CreateBy')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('updateby', models.CharField(max_length=50, db_column='UpdateBy')),
            ],
            options={
                'db_table': 'Project',
                'managed': False,
            },
        ),
    ]
