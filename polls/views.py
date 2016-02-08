from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.template.context_processors import csrf
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import connection, transaction
from django.db.models import Q
import itertools
import csv
import simplejson
import time
#import logging
from forms import *

#logger = logging.getLogger(__name__)
'''
All views interact with database by manipulating models fields directly, not creating instance from form classes
All views except index() validate inputs through self-defined validators before calling model instance save() function
'''


def index(request):
    '''
    Render index.html and submit form data to database
    '''
    c = {}
    c.update(csrf(request))  # Update csrf information
    if request.method == 'POST':
        form = AppForm(request.POST or None)

        if form.is_valid():  # Validate the input of each form fields
            cd = form.cleaned_data
            request.session["app"] = cd
            app = Application.objects.get(appid=cd['appname'])
            request.session["app"]["appname"] = app.appname

            # do not let developer to update manager, ownership, priority information
            #app.manager = cd['manager']
            #app.ownership = cd['ownership']
            #app.priority = cd['priority']

            # if field "developer" not null, django will update automatically,
            # or else it inserts this new entry
            app.developer = cd['developer']
            app.save()
            return HttpResponseRedirect('/server.html?appid=' + str(app.appid))
    else:
        form = AppForm()
    return render(request, 'index.html', {'form': form})


def app_list(request):
    '''
    According the "appid" sent by the script appselect.js to look up the related "manager", "ownership" and "priority" from database. 
    At last wrap these data to json file and send to script appselect.js to refresh page
    '''

    AppChoice = request.GET.get('appid', False)
    jsondata = []
    ManagerChoice = Application.objects.filter(
        appid=AppChoice).values_list('appid', 'manager')
    temp = {}
    temp['lable'] = ManagerChoice[0][0]
    temp['text'] = ManagerChoice[0][1]
    jsondata.append(temp)
    OwnerChoice = Application.objects.filter(
        appid=AppChoice).values_list('appid', 'ownership')
    temp = {}
    temp['lable'] = OwnerChoice[0][0]
    temp['text'] = OwnerChoice[0][1]
    jsondata.append(temp)
    PriChoice = Application.objects.filter(
        appid=AppChoice).values_list('appid', 'priority')
    temp = {}
    temp['lable'] = PriChoice[0][0]
    temp['text'] = PriChoice[0][1]
    jsondata.append(temp)
    return HttpResponse(simplejson.dumps(jsondata), content_type='application/json')


def server(request):
    '''
    Render server.html and submit user post data to database
    '''

    error = 0
    errors = []
    c = {}
    c.update(csrf(request))  # Update csrf information
    if request.method == 'POST':
        appid = request.GET.get('appid', False)
        # According the "appid" sent by url to generate the related application
        # object
        app = Application.objects.get(pk=appid)
        #form = ServerForm(request.POST or None)
        form = ServerForm(request.POST or None)

        keys = request.POST.keys()
        if len(keys) < 1:
            # User posts nothing
            return HttpResponseBadRequest("Error 400.", content_type="text/plain")
        temp_form = {}
        data = []
        # The amount of forms submitted(because each form has 5 fields)
        num = (len(keys)-2)/5

        # Store each form data to a dictionary(temp_form), then append these
        # dicts to a list called data
        for i in range(num):
            for j in range(len(keys)):
                if keys[j] != "csrfmiddlewaretoken" and keys[j] != "submit" and int(keys[j][-1]) == i:
                    temp_form[keys[j][:-1]] = request.POST[keys[j]]
            data.append(temp_form)
            temp_form = {}
        
        sid = ""
        for i in range(len(data)):
            request.session["server" + str(i)] = data[i]
            # If in database there is an entry has the same hostname or ipaddress, the code below will update that entry, or else it will
            # insert a new entry to database
            try:
                server = Server.objects.get(
                    Q(hostname=data[i]['hostname']) | Q(ipaddr=data[i]['ipaddr']))
                server.datacenter = data[i]['datacenter']
                server.status = data[i]['status']
                server.description = data[i]['description']
                server.hostname = data[i]['hostname']
                server.ipaddr = data[i]['ipaddr']
                try:
                    server.save()
                except ValidationError, e:
                    error = 1
                    errors = list(itertools.chain(*e.message_dict.values()))
            except ObjectDoesNotExist:
                try:
                    server = Server.objects.create(hostname=data[i]['hostname'], ipaddr=data[i]['ipaddr'], datacenter=data[i][
                                                   'datacenter'], status=data[i]['status'], appid=app, description=data[i]['description'])
                except ValidationError, e:
                    error = 1
                    errors = list(itertools.chain(*e.message_dict.values()))
            sid = str(server.sid) + "%20" + sid
        if error == 0:
            return HttpResponseRedirect('process.html?appid=' + appid + '&sid=' + sid)

    else:
        form = ServerForm()

    context = {
        'form': form,
        'errors': errors,
    }

    return render(request, 'server.html', context)


def process(request):
    '''
    Render process.html and submit user post data to database
    '''
    error = 0
    errors = []
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':

        appid = request.GET.get('appid', False)
        app = Application.objects.get(pk=appid)
        sid = request.GET.get('sid', False)
        sids = sid.strip().split()
        form = ProcessForm(request.POST or None)

        keys = request.POST.keys()
        if len(keys) < 1:
            return HttpResponseBadRequest("Error 400.", content_type="text/plain")
        temp_form = {}
        data = []
        num = (len(keys)-2)/8
        for i in range(num):
            for j in range(len(keys)):
                if keys[j] != "csrfmiddlewaretoken" and keys[j] != "submit" and int(keys[j][-1]) == i:
                    temp_form[keys[j][:-1]] = request.POST[keys[j]]
            data.append(temp_form)
            temp_form = {}


        for i in range(len(data)):
            request.session["process" + str(i)] = data[i]
            for j in range(len(sids)):
                # get pids, names and keywords of all processes which belong to
                # the server sent by POST data
                server = Server.objects.get(pk=sids[j])
                try:
                    temppid = server.process_set.filter(
                        sid=sids[j]).values_list('pid', 'pname', 'keywords')
                    newpid = {}
                    for x in temppid:
                        newpid[x[1]] = x[0]
                        newpid[x[2]] = x[0]


                    if newpid.has_key(data[i]['pname']) or newpid.has_key(data[i]['keywords']):
                        if newpid.has_key(data[i]['pname']):
                            pid = newpid[data[i]['pname']]
                        else:
                            pid = newpid[data[i]['keywords']]
                        process = Process.objects.get(pid=pid)
                        process.starttime = data[i]['starttime']
                        process.endtime = data[i]['endtime']
                        process.monitortime = data[i]['monitortime']
                        process.severity = data[i]['severity']
                        process.instance = data[i]['instance']
                        process.keywords = data[i]['keywords']
                        process.remark = data[i]['remark']
                        try:
                            process.save()
                        except ValidationError, e:
                            error = 1
                            errors = list(
                                itertools.chain(*e.message_dict.values()))
                    else:
                        try:
                            process = Process.objects.create(pname=data[i]['pname'], starttime=data[i]['starttime'], endtime=data[i]['endtime'], monitortime=data[
                                                             i]['monitortime'], severity=data[i]['severity'], instance=data[i]['instance'], keywords=data[i]['keywords'], remark=data[i]['remark'])
                            process.sid.add(server)
                        except ValidationError, e:
                            error = 1
                            errors = list(
                                itertools.chain(*e.message_dict.values()))
                except ObjectDoesNotExist:
                    try:
                        process = Process.objects.create(pname=data[i]['pname'], starttime=data[i]['starttime'], endtime=data[i][
                            'endtime'], monitortime=data[i]['monitortime'], severity=data[i]['severity'], instance=data[i]['instance'], keywords=data[i]['keywords'], remark=data[i]['remark'])
                        process.sid.add(server)
                    except ValidationError, e:
                        error = 1
                        errors = list(
                            itertools.chain(*e.message_dict.values()))
        if error == 0:
            return HttpResponseRedirect('log.html?appid=' + appid + '&sid=' + sid)

    else:
        form = ProcessForm()

    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'process.html', context)


def log(request):
    '''
    Render log.html and submit user post data to database
    '''
    error = 0
    errors = []
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':

        appid = request.GET.get('appid', False)
        app = Application.objects.get(pk=appid)
        sid = request.GET.get('sid', False)
        sids = sid.strip().split()
        logform = LogForm()
        logstringform = LogstringForm()

        keys = request.POST.keys()
        if len(keys) < 1:
            return HttpResponseBadRequest("Error 400.", content_type="text/plain")
        temp_form = {}
        data = []
        num = 1
        # To calculate the amount of forms submitted
        for i in range(len(keys)):
            if keys[i][-1].isdigit() and num <= int(keys[i][-1]):
                num = int(keys[i][-1])+1

        for i in range(num):
            for j in range(len(keys)):
                if keys[j] != "csrfmiddlewaretoken" and keys[j] != "submit" and int(keys[j][-1]) == i:
                    temp_form[keys[j][:-1]] = request.POST[keys[j]]
            data.append(temp_form)
            temp_form = {}


        for i in range(len(data)):
            request.session["log" + str(i)] = data[i]
            for j in range(len(sids)):
                # Get pids, names and keywords of all processes which belong to
                # the same sid sent by POST data
                server = Server.objects.get(pk=sids[j])
                try:
                    templid = server.log_set.filter(
                        sid=sids[j]).values_list('lid', 'path')
                    newlid = {}
                    for x in templid:
                        newlid[x[1]] = x[0]

                    #If there is a duplicate path in database, update the database, else create a new entry in database.
                    if newlid.has_key(data[i]['path']):
                        log = Log.objects.get(lid=newlid[data[i]['path']])
                        log.starttime = data[i]['starttime']
                        log.endtime = data[i]['endtime']
                        log.monitortime = data[i]['monitortime']
                        log.remark = data[i]['remark']
                        try:
                            log.save()
                            LogstrSave(i, log, data[i])
                        except ValidationError, e:
                            error = 1
                            errors = list(
                                itertools.chain(*e.message_dict.values()))
                    else:
                        try:
                            log = Log.objects.create(path=data[i]['path'], starttime=data[i]['starttime'], endtime=data[
                                                     i]['endtime'], monitortime=data[i]['monitortime'], remark=data[i]['remark'])
                            log.sid.add(server)
                            LogstrSave(i, log, data[i])
                        except ValidationError, e:
                            error = 1
                            errors = list(
                                itertools.chain(*e.message_dict.values()))
                except ObjectDoesNotExist:
                    try:
                        log = Log.objects.create(path=data[i]['path'], starttime=data[i]['starttime'], endtime=data[
                                                 i]['endtime'], monitortime=data[i]['monitortime'], remark=data[i]['remark'])
                        log.sid.add(server)
                        LogstrSave(i, log, data[i])
                    except ValidationError, e:
                        error = 1
                        errors = list(
                            itertools.chain(*e.message_dict.values()))
        #assert False
        if error == 0:
            return HttpResponseRedirect("confirm.html")
    else:
        # Because log and logstring are two tables in database, we need to
        # create their form instances at the same time and send their initial
        # data by context
        logform = LogForm()
        logstringform = LogstringForm()

    context = {
        'logform': logform,
        'logstringform': logstringform,
        'errors': errors
    }
    return render(request, 'log.html', context)


def LogstrSave(j, log, dict):
    '''
    Save keywords belonged to each log to database table "logstring"
    i: the handling form No.
    log: Model Log instance object
    dict: All handling form data from POST
    '''

    data = []
    # Generate (keywords, severity) pairs
    for i in range(len(dict)):
        tempstr1 = "keywords" + str(i)
        tempstr2 = "severity" + str(i)
        if dict.has_key(tempstr1) and dict.has_key(tempstr2):
            pair = (dict[tempstr1], dict[tempstr2])
            data.append(pair)

    #request.session["lstr" + str(j)] = data
    for (key, val) in data:
        try:
            logstr = Logstring.objects.get(lid=log, keywords=key)
            logstr.severity = val
            logstr.save()
        except ObjectDoesNotExist:
            logstr = Logstring.objects.create(
                lid=log, keywords=key, severity=val)
            logstr.save()


def export_processes(self):
    cursor = connection.cursor()
    try:
        cursor.execute("select appname, datacenter, hostname, ipaddr, server.status, description, pname, \
            monitortime, starttime, endtime, instance,process.severity, keywords, remark from application, server, process, \
            process_sid where application.appid=server.appid and server.sid=process_sid.server_id and process_sid.process_id=process.pid \
            order by appname,hostname,ipaddr")
        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'] = 'attachment; filename=processes_info.csv'
        writer = csv.writer(response)
        writer.writerow(['Appname', 'Datacenter', 'Hostname', 'IP', 'Server Status', 'Description', 'Process',
                         'Monitortime', 'Starttime', 'Endtime', 'Instance', 'Severity', 'Keywords', 'Remark'])
        for row in cursor.fetchall():
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], \
                'All year' if row[7] == 1 else 'All year except holidays', row[8], row[9], row[10], row[11], row[12], row[13]])
    finally:
        cursor.close()
    return response

def export_logs(self):
    cursor = connection.cursor()
    try:
        cursor.execute("select appname, datacenter, hostname, ipaddr, server.status, description, path, \
            monitortime, starttime, endtime, remark, keywords, severity from application, server, log, \
            log_sid, logstring where application.appid=server.appid and server.sid=log_sid.server_id and log_sid.log_id=log.lid and \
            log.lid = logstring.lid order by appname,hostname,ipaddr,path")
        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'] = 'attachment; filename=logs_info.csv'
        writer = csv.writer(response)
        writer.writerow(['Appname', 'Datacenter', 'Hostname', 'IP', 'Server Status', 'Description', 'Log Path',
                         'Monitortime', 'Starttime', 'Endtime', 'Remark', 'Log Keywords', 'severity'])
        for row in cursor.fetchall():
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], \
                'All year' if row[7] == 1 else 'All year except holidays', row[8], row[9], row[10], row[11], row[12]])
    finally:
        cursor.close()
    return response

def confirm(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'confirm.html')

def finish(self):
    return render_to_response('finish.html')
