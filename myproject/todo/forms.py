from django import forms
from . import models
import datetime

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'slug', 'description', 'date_time', 'status']

class UpdateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'slug', 'description', 'date_time', 'status']
