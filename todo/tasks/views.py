from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import *
from .forms import *

# Create your views here.

# class index(CreateView):
#     model = Task
#     form_class = TaskForm
#     template_name = 'tasks/list.html'


 
# class deleteTask(DeleteView):
#     model = Task
#     template_name = 'tasks/delete.html'
#     success_url = reverse_lazy('index')

# class updateTask(UpdateView):
#     model = Task
#     template_name = 'tasks/update_task.html'
#     form_class = TaskFormEdit
	

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {
     'tasks':tasks, 
     'form':form
     }
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
     'form':form
     }

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)