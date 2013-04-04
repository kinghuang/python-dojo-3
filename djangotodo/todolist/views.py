from django.shortcuts import render
from todolist.models import Task
from forms import NewTaskForm, TaskForm, TaskFormSet
from django.core.exceptions import PermissionDenied

def list(request):
	form = NewTaskForm()
	formset = TaskFormSet()
	
	if request.method == "POST":
		if (request.POST['button'] == 'Update!'):
			formset = TaskFormSet(request.POST)
			if formset.is_valid():
				formset.save()
				formset = TaskFormSet()
		else:
			form = NewTaskForm(request.POST)
			if form.is_valid():
				form.save()
				# make sure to return use a clean form for the resulting page
				form = NewTaskForm()

	elif request.method != 'GET':
		raise PermissionDenied('Only GET and POST methods are allowed')

	return render(request, 'todolist/list-view.html', {
    	'tasks': Task.objects.all(),
    	'form': form,
    	'formset': formset
    })
