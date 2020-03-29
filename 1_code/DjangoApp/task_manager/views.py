from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.views import generic

import task_manager.task_manager_db_helper as tm_db

def index(request):
    tasks = tm_db.get_all_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_manager/index.html', context)

def edit(request):
	task = tm_db.get_task(request.GET['id'])
	context = {'task': task}
	return render(request, 'task_manager/edit.html', context)
	
def modify(request):
	old = tm_db.get_task(request.POST['taskID'])
	tm_db.modify_task(request.POST['taskID'], request.POST['taskName'], request.POST['description'], request.POST['state'], request.POST['employeeID'], request.POST['timeCreated'], request.POST['timeCompleted'])
	new = tm_db.get_task(request.POST['taskID'])
	context = {'old': old,'new': new}
	return render(request, 'task_manager/modify.html', context)