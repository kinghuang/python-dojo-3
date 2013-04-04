from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from models import Task

class NewTaskForm(ModelForm):
	description = forms.CharField()

	class Meta:
		model = Task	
		exclude = ('completed',)

class TaskForm(ModelForm):
	description = forms.CharField()

	class Meta:
		model = Task

TaskFormSet = modelformset_factory(Task, extra=0, form=TaskForm)