from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'team']
        widgets = {
            'task': forms.Textarea
        }


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name_team', 'rating']

class EnterForm(forms.ModelForm):
    pass

class RegForm(forms.ModelForm):
    pass