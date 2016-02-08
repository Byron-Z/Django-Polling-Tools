from django.shortcuts import render
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django import forms
from .models import *
from .forms import SearchForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection, transaction


class AppAdmin(admin.ModelAdmin):
    list_display = (
        "appid", "appname", "manager", "ownership", "priority", "developer")
    search_fields = ("appname", "manager", "developer")
    list_filter = ("manager", "developer", )

    class Meta:
        model = Application

admin.site.register(Application, AppAdmin)


class ServerAdmin(admin.ModelAdmin):
    list_display = (
        "sid", "datacenter", "hostname", "ipaddr", "status", "appid", "description")
    search_fields = ("datacenter", "hostname", "ipaddr", "appid__appname")
    list_filter = ("datacenter", "appid__appname", )

    class Meta:
        model = Server

admin.site.register(Server, ServerAdmin)


class ProcessAdmin(admin.ModelAdmin):
    list_display = ("pid", "pname", "starttime", "endtime",
                    "monitortime", "severity", "instance", "keywords", "remark")
    search_fields = ("pname", "keywords", "severity", "sid__hostname", "sid__ipaddr", "sid__appid__appname")
    list_filter = ("severity", "sid__appid__appname", )

    class Meta:
        model = Process

admin.site.register(Process, ProcessAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = (
        "lid", "path", "starttime", "endtime", "monitortime", "remark")
    search_fields = ("path", "sid__hostname", "sid__ipaddr", "sid__appid__appname")
    list_filter = ("sid__appid__appname", )

    class Meta:
        model = Log

admin.site.register(Log, LogAdmin)


class LogstringAdmin(admin.ModelAdmin):
    list_display = ("lsid", "lid", "keywords", "severity")
    search_fields = ("keywords", "severity", "lid__path", "lid__sid__hostname", "lid__sid__ipaddr", "lid__sid__appid__appname")
    list_filter = ("lid__sid__appid__appname", )

    class Meta:
        model = Logstring

admin.site.register(Logstring, LogstringAdmin)

class SearchAdmin(admin.ModelAdmin):
    search_template = 'admin/polls/search/search.html'
    
    def get_urls(self):
        urls = super(SearchAdmin, self).get_urls()
        search_urls = [url(r'^$', self.admin_site.admin_view(self.search), name='polls_search'),]
        return search_urls + urls

    def search(self, request):
        if request.method == 'POST':
            query_string = request.POST.get('query', '')
            appid = request.POST.get('appname', False)
            form = SearchForm(request.POST or None)
            if form.is_valid():
                cursor = connection.cursor()
                if request.POST.has_key("process"):
                    if query_string != '':
                        try:
                            query_string = "'%%"+ query_string + "%%'"
                            cursor.execute("select datacenter, hostname, ipaddr, server.status, description, pname, \
                                monitortime, starttime, endtime, instance,process.severity, keywords, remark \
                                from application, server, process, process_sid \
                                where application.appid=%s and (hostname like %s or ipaddr like %s) and \
                                application.appid=server.appid and server.sid=process_sid.server_id and process_sid.process_id=process.pid \
                                order by appname,hostname,ipaddr" % (appid, query_string, query_string))
                            data = cursor.fetchall()
                        finally:
                            cursor.close()
                    else:
                        try:
                            cursor.execute("select datacenter, hostname, ipaddr, server.status, description, pname, \
                                monitortime, starttime, endtime, instance,process.severity, keywords, remark \
                                from application, server, process, process_sid \
                                where application.appid=%s and application.appid=server.appid and server.sid=process_sid.server_id \
                                and process_sid.process_id=process.pid \
                                order by appname,hostname,ipaddr" % appid)
                            data = cursor.fetchall()
                        finally:
                            cursor.close()
                    context = {
                            'appid' : appid,
                            'form' : form,
                            'data' : data,
                        }
                    return render(request, 'admin/polls/search/search_process.html', context)
                else:
                    if query_string != '':
                        try:
                            query_string = "'%%"+ query_string + "%%'"
                            cursor.execute("select datacenter, hostname, ipaddr, server.status, description, path, \
                                monitortime, starttime, endtime, remark, keywords, severity from application, server, log, \
                                log_sid, logstring where application.appid=%s and server.appid=application.appid and (hostname like %s or ipaddr like %s) \
                                and server.sid=log_sid.server_id and log_sid.log_id=log.lid and log.lid = logstring.lid \
                                order by appname,hostname,ipaddr,path" % (appid, query_string, query_string))
                            data = cursor.fetchall()
                        finally:
                            cursor.close()
                    else:
                        try:
                            cursor.execute("select datacenter, hostname, ipaddr, server.status, description, path, \
                                monitortime, starttime, endtime, remark, keywords, severity from application, server, log, \
                                log_sid, logstring where application.appid=%s and server.appid=application.appid and server.sid=log_sid.server_id and \
                                log_sid.log_id=log.lid and log.lid = logstring.lid order by appname,hostname,ipaddr,path" % appid)
                            data = cursor.fetchall()
                        finally:
                            cursor.close()

                    context = {
                            'appid' : appid,
                            'form' : form,
                            'data' : data,
                        }
                    return render(request, 'admin/polls/search/search_log.html', context)
        else:
            form = SearchForm()
            context = {
            'form' : form,
            }
        return render(request, 'admin/polls/search/search_log.html', context)

    class Meta:
        model = Search

admin.site.register(Search, SearchAdmin)
