# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

@login_required
def index(request):
	if request.method == 'GET':
		form = TaskForm()
	elif request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():

			#create the task object but not saving to database yet
			obj = form.save(commit=False)

			#assign the task to the current use
			obj.user = request.user

			#save
			obj.save()
		
	tasks = Task.objects.filter(user=request.user)

	return render(request, 'task/index.html', {'tasks': tasks, 'form': form})


#need model_form.html template to use the updateview
# in this case, task_form.html
class TaskUpdate(UpdateView):
	model = Task
	fields = ['task_name', 'description', 'is_completed']

class TaskDelete(DeleteView):
	model = Task
	success_url = reverse_lazy('task:index')

def complete(request, pk):
	task = Task.objects.get(pk=pk)
	if task.is_completed == True:
		task.is_completed = False
	else:
		task.is_completed = True
	task.save()

	return redirect('task:index')








