from django.shortcuts import render
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django import forms
from .forms import TaskProgressForm
#from tom import models as tom_models
from .models import *
from django.db.models.base import ModelBase
from django.db import connection, transaction
import pyodbc

# Register your models here.
'''for name, var in tom_models.__dict__.items():
    #print name, var, "!!!!", type(var)
    if type(var) is ModelBase and name != "Tasks":
        admin.site.register(var)'''

class AppAdmin(admin.ModelAdmin):
    #list_display = Applications._meta.get_all_field_names()
    list_display = ("appid", "appname", "appregistryid", "appoperatingsystem", "appownergroup", "appoperationsuppgroup", "appdeploysuppgroup", "appdevmanager", "appteamleadsupport", "appteamleadtechops", "apptransitioncomplexity", "appclassregsci", "appmarketedge", "appcrossdatacenterdependencies", "appsinglepointoffailure", "appexternallyfacing", "appbehindwaf", "applatencysensitive", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Applications

admin.site.register(Applications, AppAdmin)

class ClassregscisAdmin(admin.ModelAdmin):
    list_display = ("classregsci_id", "classregsci_desc", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Classregscis

admin.site.register(Classregscis, ClassregscisAdmin)

class ComplexitiesAdmin(admin.ModelAdmin):
    list_display = ("complexityid", "complexitydesc", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Complexities

admin.site.register(Complexities, ComplexitiesAdmin)

class ComponentsAdmin(admin.ModelAdmin):
    list_display = ("componentid", "componentname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Components

admin.site.register(Components, ComponentsAdmin)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ("contactid", "contactfirstname", "contactlastname", "contactemail", "groupid", "createdate", "createby", "updatedate", "updateby")
    
    class Meta:
        model = Contacts

admin.site.register(Contacts, ContactsAdmin)

class DatasourcesAdmin(admin.ModelAdmin):
    list_display = ("datasourceid", "datasourcename", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Datasources

admin.site.register(Datasources, DatasourcesAdmin)

class EnvironmentsAdmin(admin.ModelAdmin):
    list_display = ("environmentid", "environmentname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Environments

admin.site.register(Environments, EnvironmentsAdmin)

class GroupsAdmin(admin.ModelAdmin):
    list_display = ("groupid", "groupname", "groupnasdaqdeptid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Groups

admin.site.register(Groups, GroupsAdmin)

class JoinappcomponentAdmin(admin.ModelAdmin):
    list_display = ("appid", "componentid", "componentleaddeveloper", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappcomponent

admin.site.register(Joinappcomponent, JoinappcomponentAdmin)

class JoinappdatasourceAdmin(admin.ModelAdmin):
    list_display = ("appid", "datasourceid", "createdate", "createby", "updatedate", "updateby")
    class Meta:
        model = Joinappdatasource

admin.site.register(Joinappdatasource, JoinappdatasourceAdmin)

class JoinappenvironmentAdmin(admin.ModelAdmin):
    list_display = ("appid", "environmentid", "flaggedexemptby", "flaggedexempton", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappenvironment

admin.site.register(Joinappenvironment, JoinappenvironmentAdmin)

class JoinappmonitorAdmin(admin.ModelAdmin):
    list_display = ("appid", "monitorid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappmonitor

admin.site.register(Joinappmonitor, JoinappmonitorAdmin)

class JoinappnetworksegmentAdmin(admin.ModelAdmin):
    list_display = ("appid", "networksegmentid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappnetworksegment

admin.site.register(Joinappnetworksegment, JoinappnetworksegmentAdmin)

class JoinappoperationwindowAdmin(admin.ModelAdmin):
    list_display = ("appid", "operationwindowid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappoperationwindow

admin.site.register(Joinappoperationwindow, JoinappoperationwindowAdmin)

class JoinappproviderconsumerAdmin(admin.ModelAdmin):
    list_display = ("providerappid", "consumerappid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Joinappproviderconsumer

admin.site.register(Joinappproviderconsumer, JoinappproviderconsumerAdmin)

class MilestonesAdmin(admin.ModelAdmin):
    list_display = ("milestoneid", "milestonedesc", "milestonerank", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Milestones

admin.site.register(Milestones, MilestonesAdmin)

class MonitorsAdmin(admin.ModelAdmin):
    list_display = ("monitorid", "monitorname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Monitors

admin.site.register(Monitors, MonitorsAdmin)

class NetworksegmentsAdmin(admin.ModelAdmin):
    list_display = ("networksegmentid", "networksegmentname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Networksegments

admin.site.register(Networksegments, NetworksegmentsAdmin)

class OperatingsystemsAdmin(admin.ModelAdmin):
    list_display = ("operatingsystemid", "operatingsystemname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Operatingsystems

admin.site.register(Operatingsystems, OperatingsystemsAdmin)


class OperationwindowsAdmin(admin.ModelAdmin):
    list_display = ("operationwindowid", "operationwindowname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Operationwindows

admin.site.register(Operationwindows, OperationwindowsAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("appid", "apppriority", "lastreviewdate", "lastreviewby", "projectnotes", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)

class TaskgroupsAdmin(admin.ModelAdmin):
    list_display = ("taskgroupid", "taskgroupname", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Taskgroups

admin.site.register(Taskgroups, TaskgroupsAdmin)

class TasktypesAdmin(admin.ModelAdmin):
    list_display = ("tasktypeid", "tasktypename", "milestoneid", "taskrank", "taskgroupid", "createdate", "createby", "updatedate", "updateby")

    class Meta:
        model = Tasktypes

admin.site.register(Tasktypes, TasktypesAdmin)


class TasksAdmin(admin.ModelAdmin):
    #list_display = Tasks._meta.get_all_field_names()

    def appid__appname(self, obj):
        return obj.appid.appname
    appid__appname.short_description = 'appname'
    appid__appname.admin_order_field = 'appid__appname'

    def tasktypeid__tasktypename(self, obj):
        return str(obj.tasktypeid.tasktypename)
    tasktypeid__tasktypename.short_description = 'tasktypename'
    tasktypeid__tasktypename.admin_order_field = 'tasktypeid__tasktypename'

    def assignedto__contactfirstname(self, obj):
    	if obj.assignedto:
            return str(obj.assignedto.contactfirstname)
        else:
        	return None
    assignedto__contactfirstname.short_description = 'assignedto'
    assignedto__contactfirstname.admin_order_field = 'assignedto__contactfirstname'

    def flaggedexemptby__contactfirstname(self, obj):
    	if obj.flaggedexemptby:
        	return str(obj.flaggedexemptby.contactfirstname)
        else:
        	return None
    flaggedexemptby__contactfirstname.short_description = 'flaggedexemptby'
    flaggedexemptby__contactfirstname.admin_order_field = 'flaggedexemptby__contactfirstname'


    list_display = ("appid__appname", "tasktypeid__tasktypename", "assignedto__contactfirstname", "originaltargetdate", "currenttargetdate", "taskinprogress",
                    "completionpercent", "completiondate", "tasknotes", "createdate", "createby", "updatedate", "updateby", "flaggedexemptby__contactfirstname", "flaggedexempton")
    search_fields = ("appid__appname", "tasktypeid__tasktypename", "assignedto__contactfirstname", "originaltargetdate", "currenttargetdate", "taskinprogress",
                    "completionpercent", "completiondate", "tasknotes", "createdate", "createby", "updatedate", "updateby", "flaggedexemptby__contactfirstname", "flaggedexempton")
    list_filter = ("appid", "tasktypeid", "assignedto")

    class Meta:
        model = Tasks

admin.site.register(Tasks, TasksAdmin)

class TaskProgressAdmin(admin.ModelAdmin):
    
    def get_urls(self):
        urls = super(TaskProgressAdmin, self).get_urls()
        tp_urls = [url(r'^$', self.admin_site.admin_view(self.taskprogress), name='tom_taskprogress'),]
        return tp_urls + urls

    def taskprogress(self, request):
        click = False
        if request.method == 'POST':
            number = request.POST.get('number', '')
            app = request.POST.get('appname', '')
            click = True
            data, num, descript = "", 0 , ""
            form = TaskProgressForm(request.POST or None)
            if form.is_valid():
                #cursor = connection.cursor()
                cnxn = pyodbc.connect('dsn=sqlserver;DATABASE=TOM;UID=wildag;PWD=buystevebeer')
                cursor = cnxn.cursor()
                if len(number) != 0 and len(app) != 0:
                    sql = "select Applications.AppID, Applications.AppName, stuff(( \
                        select top %s '@ '+TaskTypes.TaskTypeName+' '+ cast(Tasks.CompletionPercent as varchar)+'%%' from Tasks, TaskTypes \
                        where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID order by Tasks.CompletionPercent desc FOR XML PATH('')),1,1,'') as tasks \
                        from Applications where Applications.AppID=? group by Applications.AppID, Applications.AppName order by Applications.AppID" % (number,)
                    cursor.execute(sql, app)
                    data = cursor.fetchall()
                    
                elif len(number) != 0 and len(app) == 0:
                    cursor.execute("select Applications.AppID, Applications.AppName, stuff(( \
                        select top %s '@ '+TaskTypes.TaskTypeName+' '+ cast(Tasks.CompletionPercent as varchar)+'%%' from Tasks, TaskTypes \
                        where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID order by Tasks.CompletionPercent desc FOR XML PATH('')),1,1,'') as tasks \
                        from Applications group by Applications.AppID, Applications.AppName order by Applications.AppID" % (number,))
                    data = cursor.fetchall()

                elif len(number) == 0 and len(app) != 0:
                    cursor.execute("select Applications.AppID, Applications.AppName, stuff(( \
                        select '@ '+ cast(Tasks.CompletionPercent as varchar)+'%' from Tasks, TaskTypes \
                        where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID FOR XML PATH('')),1,1,'') as tasks \
                        from Applications where Applications.AppID=? group by Applications.AppID, Applications.AppName order by Applications.AppID", app)
                    data = cursor.fetchall()

                else:
                    cursor.execute("select Applications.AppID, Applications.AppName, stuff(( \
                        select '@ '+ cast(Tasks.CompletionPercent as varchar) + '%' from Tasks, TaskTypes \
                        where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID FOR XML PATH('')),1,1,'') as tasks \
                        from Applications group by Applications.AppID, Applications.AppName order by Applications.AppID")
                    data = cursor.fetchall()

                for items in data:
                    items[2] = items[2].split("@ ")

                try:
                    cursor.execute("select top 1 stuff(( \
                        select '@ '+TaskTypes.TaskTypeName from Tasks, TaskTypes \
                        where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID FOR XML PATH('')),1,1,'') as tasks \
                        from Applications group by Applications.AppID order by Applications.AppID")
                    rownames = cursor.fetchall()
                finally:
                    cursor.close()
                descript = str(rownames[0][0]).split("@ ")

                if len(number) != 0:
                    num = int(number)
                else:
                    num = 61

            context = {
                    'form' : form,
                    'data' : data,
                    'num' : range(num), 
                    'descript' : descript,
                    'click' : click,
                }
        else:
            form = TaskProgressForm()
            context = {
            'form' : form,
            }
        return render(request, 'admin/tom/taskprogress/taskprogress.html', context)

    class Meta:
        model = TaskProgress

admin.site.register(TaskProgress, TaskProgressAdmin)
