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


class Applications(models.Model):
    appid = models.CharField(db_column='AppID', primary_key=True, max_length=15)  # Field name made lowercase.
    appname = models.CharField(db_column='AppName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appregistryid = models.CharField(db_column='AppRegistryID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appoperatingsystem = models.CharField(db_column='AppOperatingSystem', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appownergroup = models.CharField(db_column='AppOwnerGroup', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appoperationsuppgroup = models.CharField(db_column='AppOperationSuppGroup', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appdeploysuppgroup = models.CharField(db_column='AppDeploySuppGroup', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appdevmanager = models.CharField(db_column='AppDevManager', max_length=15)  # Field name made lowercase.
    appteamleadsupport = models.CharField(db_column='AppTeamLeadSupport', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appteamleadtechops = models.CharField(db_column='AppTeamLeadTechOps', max_length=15, blank=True, null=True)  # Field name made lowercase.
    apptransitioncomplexity = models.CharField(db_column='AppTransitionComplexity', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appclassregsci = models.CharField(db_column='AppClassRegSCI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appmarketedge = models.NullBooleanField(db_column='AppMarketEdge')  # Field name made lowercase.
    appcrossdatacenterdependencies = models.NullBooleanField(db_column='AppCrossDataCenterDependencies')  # Field name made lowercase.
    appsinglepointoffailure = models.NullBooleanField(db_column='AppSinglePointOfFailure')  # Field name made lowercase.
    appexternallyfacing = models.NullBooleanField(db_column='AppExternallyFacing')  # Field name made lowercase.
    appbehindwaf = models.NullBooleanField(db_column='AppBehindWAF')  # Field name made lowercase.
    applatencysensitive = models.NullBooleanField(db_column='AppLatencySensitive')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Applications'

    def __unicode__(self):
        return ('%s' % self.appname)


class Classregscis(models.Model):
    classregsci_id = models.CharField(db_column='ClassRegSCI_ID', primary_key=True, max_length=15)  # Field name made lowercase.
    classregsci_desc = models.CharField(db_column='ClassRegSCI_Desc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClassRegSCIs'


class Complexities(models.Model):
    complexityid = models.CharField(db_column='ComplexityID', primary_key=True, max_length=15)  # Field name made lowercase.
    complexitydesc = models.CharField(db_column='ComplexityDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Complexities'


class Components(models.Model):
    componentid = models.CharField(db_column='ComponentID', primary_key=True, max_length=15)  # Field name made lowercase.
    componentname = models.CharField(db_column='ComponentName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Components'

    def __unicode__(self):  
        return ('%s' % self.componentname)


class Contacts(models.Model):
    contactid = models.CharField(db_column='ContactID', primary_key=True, max_length=15)  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='ContactFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactlastname = models.CharField(db_column='ContactLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contacts'

    def __unicode__(self):  
        return ("%s %s" % (self.contactfirstname, self.contactlastname))


class Datasources(models.Model):
    datasourceid = models.CharField(db_column='DataSourceID', primary_key=True, max_length=15)  # Field name made lowercase.
    datasourcename = models.CharField(db_column='DataSourceName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSources'

    def __unicode__(self):  
        return ('%s' % self.datasourcename)


class Environments(models.Model):
    environmentid = models.CharField(db_column='EnvironmentID', primary_key=True, max_length=15)  # Field name made lowercase.
    environmentname = models.CharField(db_column='EnvironmentName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Environments'

    def __unicode__(self):  
        return ('%s' % self.environmentname)


class Groups(models.Model):
    groupid = models.CharField(db_column='GroupID', primary_key=True, max_length=15)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    groupnasdaqdeptid = models.IntegerField(db_column='GroupNasdaqDeptID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'

    def __unicode__(self):  
        return ('%s' % self.groupname)


class Joinappcomponent(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    componentid = models.ForeignKey(Components, db_column='ComponentID')  # Field name made lowercase.
    componentleaddeveloper = models.ForeignKey(Contacts, db_column='ComponentLeadDeveloper', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppComponent'
        unique_together = (('appid', 'componentid'),)


class Joinappdatasource(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    datasourceid = models.ForeignKey(Datasources, db_column='DataSourceID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppDataSource'
        unique_together = (('appid', 'datasourceid'),)


class Joinappenvironment(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    environmentid = models.ForeignKey(Environments, db_column='EnvironmentID')  # Field name made lowercase.
    flaggedexemptby = models.ForeignKey(Contacts, db_column='FlaggedExemptBy', blank=True, null=True)  # Field name made lowercase.
    flaggedexempton = models.DateTimeField(db_column='FlaggedExemptOn', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppEnvironment'
        unique_together = (('appid', 'environmentid'),)


class Joinappmonitor(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    monitorid = models.ForeignKey('Monitors', db_column='MonitorID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppMonitor'
        unique_together = (('appid', 'monitorid'),)


class Joinappnetworksegment(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    networksegmentid = models.ForeignKey('Networksegments', db_column='NetworkSegmentID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppNetworkSegment'
        unique_together = (('appid', 'networksegmentid'),)


class Joinappoperationwindow(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    operationwindowid = models.ForeignKey('Operationwindows', db_column='OperationWindowID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppOperationWindow'
        unique_together = (('appid', 'operationwindowid'),)


class Joinappproviderconsumer(models.Model):
    providerappid = models.ForeignKey(Applications, related_name='providerappid', db_column='ProviderAppID')  # Field name made lowercase.
    consumerappid = models.ForeignKey(Applications, related_name='consumerappid', db_column='ConsumerAppID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JoinAppProviderConsumer'
        unique_together = (('providerappid', 'consumerappid'),)


class Milestones(models.Model):
    milestoneid = models.CharField(db_column='MilestoneID', primary_key=True, max_length=15)  # Field name made lowercase.
    milestonedesc = models.CharField(db_column='MilestoneDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    milestonerank = models.SmallIntegerField(db_column='MilestoneRank', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Milestones'

    def __unicode__(self):  
        return ('%s' % self.milestonedesc)


class Monitors(models.Model):
    monitorid = models.CharField(db_column='MonitorID', primary_key=True, max_length=15)  # Field name made lowercase.
    monitorname = models.CharField(db_column='MonitorName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Monitors'

    def __unicode__(self):  
        return ('%s' % monitorname)


class Networksegments(models.Model):
    networksegmentid = models.CharField(db_column='NetworkSegmentID', primary_key=True, max_length=15)  # Field name made lowercase.
    networksegmentname = models.CharField(db_column='NetworkSegmentName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NetworkSegments'

    def __unicode__(self):  
        return ('%s' % networksegmentname)


class Operatingsystems(models.Model):
    operatingsystemid = models.CharField(db_column='OperatingSystemID', primary_key=True, max_length=15)  # Field name made lowercase.
    operatingsystemname = models.CharField(db_column='OperatingSystemName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperatingSystems'

    def __unicode__(self):  
        return ('%s' % operatingsystemname)


class Operationwindows(models.Model):
    operationwindowid = models.CharField(db_column='OperationWindowID', primary_key=True, max_length=15)  # Field name made lowercase.
    operationwindowname = models.CharField(db_column='OperationWindowName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperationWindows'

    def __unicode__(self):  
        return ('%s' % operationwindowname)


class Project(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID', primary_key=True)  # Field name made lowercase.
    apppriority = models.SmallIntegerField(db_column='AppPriority', blank=True, null=True)  # Field name made lowercase.
    lastreviewdate = models.DateTimeField(db_column='LastReviewDate', blank=True, null=True)  # Field name made lowercase.
    lastreviewby = models.CharField(db_column='LastReviewBy', max_length=15, blank=True, null=True)  # Field name made lowercase.
    projectnotes = models.TextField(db_column='ProjectNotes', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'


class Taskgroups(models.Model):
    taskgroupid = models.CharField(db_column='TaskGroupID', primary_key=True, max_length=15)  # Field name made lowercase.
    taskgroupname = models.CharField(db_column='TaskGroupName', max_length=100)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskGroups'

    def __unicode__(self):  
        return ('%s' % taskgroupname)


class Tasktypes(models.Model):
    tasktypeid = models.CharField(db_column='TaskTypeID', primary_key=True, max_length=15)  # Field name made lowercase.
    tasktypename = models.CharField(db_column='TaskTypeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    milestoneid = models.ForeignKey(Milestones, db_column='MilestoneID', blank=True, null=True)  # Field name made lowercase.
    taskrank = models.SmallIntegerField(db_column='TaskRank', blank=True, null=True)  # Field name made lowercase.
    taskgroupid = models.ForeignKey(Taskgroups, db_column='TaskGroupID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.CharField(db_column='CreateBy', max_length=50)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.CharField(db_column='UpdateBy', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTypes'

    def __unicode__(self):  
        return ('%s' % self.tasktypename)


class Tasks(models.Model):
    appid = models.ForeignKey(Applications, db_column='AppID')  # Field name made lowercase.
    tasktypeid = models.ForeignKey(Tasktypes, db_column='TaskTypeID')  # Field name made lowercase.
    assignedto = models.ForeignKey(Contacts, db_column='AssignedTo', related_name='assignedto', blank=True, null=True)  # Field name made lowercase.
    originaltargetdate = models.DateTimeField(db_column='OriginalTargetDate', blank=True, null=True)  # Field name made lowercase.
    currenttargetdate = models.DateTimeField(db_column='CurrentTargetDate', blank=True, null=True)  # Field name made lowercase.
    taskinprogress = models.BooleanField(db_column='TaskInProgress')  # Field name made lowercase.
    completionpercent = models.SmallIntegerField(db_column='CompletionPercent')  # Field name made lowercase.
    completiondate = models.DateTimeField(db_column='CompletionDate', blank=True, null=True)  # Field name made lowercase.
    tasknotes = models.TextField(db_column='TaskNotes', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    createby = models.TextField(db_column='CreateBy')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    updateby = models.TextField(db_column='UpdateBy')  # Field name made lowercase.
    flaggedexemptby = models.ForeignKey(Contacts, db_column='FlaggedExemptBy', related_name='flaggedexemptby', blank=True, null=True)  # Field name made lowercase.
    flaggedexempton = models.DateTimeField(db_column='FlaggedExemptOn', blank=True, null=True)  # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tasks'
        unique_together = (('appid', 'tasktypeid'),)

    def __unicode__(self):  
        return ('%s-%s-%s-%s' % (self.appid, self.tasktypeid, self.assignedto, self.flaggedexemptby)) 


class TaskProgress(Applications):

    class Meta:
        proxy=True
        verbose_name = 'TaskProgress'
        verbose_name_plural = 'TaskProgress'