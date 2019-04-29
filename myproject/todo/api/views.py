from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from ..models import Task

def task_list(request):
    tasks = Task.objects.all()
    data = {"results": list(tasks.values('title', 'slug', 'description', 'date_time', 'created', 'modified', 'status'))}
    return JsonResponse(data)

def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    data = {'results': {
        'title': task.title,
        'slug': task.slug,
        'description': task.description,
        'date_time': task.date_time,
        'created': task.created,
        'modified': task.modified,
        'status': task.status,
    }}
    return JsonResponse(data)
