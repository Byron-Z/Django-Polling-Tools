"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = 'TSS Monitor Administration'
admin.site.site_title = 'TSS Monitor Administration'
admin.site.index_title = ''
urlpatterns = [
    url(r'^$', 'polls.views.index', name='index'),
    url(r'^index.html$', 'polls.views.app_list', name='app_list'),
    url(r'^server.html$', 'polls.views.server', name='server'),
    url(r'^process.html$', 'polls.views.process', name='process'),
    url(r'^log.html$', 'polls.views.log', name='log'),
    url(r'^confirm.html$', 'polls.views.confirm', name='confirm'),
    url(r'^finish.html$', 'polls.views.finish', name='finish'),
    url(r'^admin/polls/search/export_processes/$', 'polls.views.export_processes', name='export_processes'),
    url(r'^admin/polls/search/export_logs/$', 'polls.views.export_logs', name='export_logs'),
    url(r'^admin/tom/taskprogress/export_tasks/$', 'tom.views.export_tasks', name='export_tasks'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
