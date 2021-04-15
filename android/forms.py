from django import forms
from .models import Task, App
from .category import Choice


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('screenshot',)

class AppForm(forms.ModelForm):
    app_category = forms.ChoiceField(choices = Choice, required = True)
    sub_category = forms.ChoiceField(choices = Choice, required = True)
    
    class Meta:
        model = App
        fields = ('name', 'applink','points','img',)