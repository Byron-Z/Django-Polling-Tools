from django import forms
from models import *

class TaskProgressForm(forms.ModelForm):
    number = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(TaskProgressForm, self).__init__(*args, **kwargs)
        app=[(str(obj[0]), obj[1].format('utf8')) for obj in Applications.objects.all().values_list('appid','appname')]
        app.insert(0,('',''))
        self.fields['appname'] = forms.ChoiceField(choices=app)
        self.fields['appname'].required = False
        
    '''def save(self, commit=True):
        number = self.cleaned_data.get('number', None)
        return super(TaskProgressForm, self).save(commit=commit)'''

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(number) != 0 and int(number) <= 0:
            raise forms.ValidationError(u'The input number is invalid!')
        return number


    class Meta:
        model = TaskProgress
        fields = ('appname', )