from django import forms
from models import *
import os
import re
#import logging

#logger = logging.getLogger(__name__)

class AppForm(forms.ModelForm):

    def clean_developer(self):
        name = self.cleaned_data['developer']
        if re.match(r'^[a-zA-Z]+[a-zA-Z \';.]*$', name) == None:
            raise forms.ValidationError(u'The input name is invalid!')
        return name

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        #self.fields['appname'] = forms.ModelChoiceField(queryset=Application.objects.all())
        #widget = forms.Select(attrs={'class':'select', 'onChange':'getCityOptions(this.value)'}),
        self.fields['appname'] = forms.ChoiceField(choices=[(str(obj[0]), obj[1]) for obj in Application.objects.all().values_list('appid','appname').order_by('appname')])
        self.fields['manager'] = forms.ChoiceField(choices=[(obj[0], obj[0]) for obj in Application.objects.all().values_list('manager').distinct()])
        self.fields['ownership'] = forms.ChoiceField(choices=[(obj[0], obj[0]) for obj in Application.objects.all().values_list('ownership').distinct()])
        self.fields['priority'] = forms.ChoiceField(choices=[(obj[0], obj[0]) for obj in Application.objects.all().values_list('priority').distinct()])
    class Meta:
        model = Application
        fields = ('appid', 'appname', 'manager', 'ownership', 'priority', 'developer')


class ServerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        dc = [('Carteret','Carteret'), ('Ashburn','Ashburn'), ('Secaucus','Secaucus'), ('Chicago','Chicago'),]
        ServerStatus = [('Hot','Hot'), ('Hot Standby', 'Hot Standby'), ('Cold Standby', 'Cold Standby'),]
        self.fields['datacenter'] = forms.ChoiceField(choices=dc)
        self.fields['status'] = forms.ChoiceField(choices=ServerStatus)
        self.fields['description'].required = False
        #self.fields['appid'] = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Server
        fields = ('sid','datacenter', 'hostname', 'ipaddr', 'status', 'description','appid')
        #exclude = ('appid',)



class ProcessForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)
        monitortime = [('1','All year'), ('2','All year except holidays'),]
        #runningtime = [('1','24/7'), ('2','Period'),]
        self.fields['monitortime'] = forms.ChoiceField(choices=monitortime)
        #self.fields['runningtime'] = forms.ChoiceField(choices=runningtime)
        self.fields['severity'] = forms.ChoiceField(choices=[(obj['severity'], obj['severity']) for obj in Severity.objects.all().values('severity')])
        self.fields['remark'].required = False
        self.fields['starttime'] = forms.TimeField(input_formats=['%H:%M:%S'])
        self.fields['endtime'] = forms.TimeField(input_formats=['%H:%M:%S'])
        self.fields['remark'].required = False

    class Meta:
        model = Process
        fields = ('pid', 'pname', 'starttime', 'endtime', 'monitortime', 'severity', 'sid', 'instance', 'keywords', 'remark')
        #exclude = ('sid',)


class LogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)
        monitortime = [('1','All year'), ('2','All year except holidays'),]
        self.fields['monitortime'] = forms.ChoiceField(choices=monitortime)
        self.fields['remark'].required = False


    class Meta:
        model = Log
        fields = ('lid', 'path', 'starttime', 'endtime', 'monitortime', 'remark')


class LogstringForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LogstringForm, self).__init__(*args, **kwargs)
        self.fields['severity'] = forms.ChoiceField(choices=[(obj['severity'], obj['severity']) for obj in Severity.objects.all().values('severity')])

    class Meta:
        model = Logstring
        fields = ('lsid', 'lid', 'keywords', 'severity')


class SearchForm(forms.ModelForm):

    query = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['appname'] = forms.ChoiceField(choices=[(str(obj[0]), obj[1]) for obj in Application.objects.all().values_list('appid','appname').order_by('appname')])

    class Meta:
        model = Search
        fields = ('appname',)       

