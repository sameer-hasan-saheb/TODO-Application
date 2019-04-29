from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^task_list/$', views.task_list, name='task_list'),
url(r'^task/(?P<slug>[\w-]+)/$', views.task_detail, name='task_detail'),
]
