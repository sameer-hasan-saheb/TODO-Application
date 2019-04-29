from django.conf.urls import url
from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.task_list, name="list"),
    url(r'^create/$', views.task_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.task_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/update/$', views.task_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.task_delete, name="delete"),
]
