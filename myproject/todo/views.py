from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Task
from . import forms

def task_list(request):
    tasks = Task.objects.filter(is_deleted=False)
    return render(request, 'todo/task_list.html', { 'tasks': tasks })

def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug, is_deleted=False)
    return render(request, 'todo/task_detail.html', { 'task': task })

def task_create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            # save article to db
            #instance = form.save(commit=False)
            #instance.author = request.user
            #instance.save()
            form.save()
            return redirect('todo:list')
    else:
        form = forms.CreateTask()
    return render(request, 'todo/task_create.html', { 'form': form })

def task_delete(request, slug):
    task = get_object_or_404(Task, slug=slug, is_deleted=False)
    task.is_deleted = True
    task.save()
    return redirect('todo:list')

def task_update(request, slug):
    task = get_object_or_404(Task, slug=slug, is_deleted=False)
    if request.method == 'POST':
        form = forms.UpdateTask(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    else:
        form = forms.UpdateTask(instance=task)
    return render(request, 'todo/task_update.html', { 'form': form, 'task': task })
