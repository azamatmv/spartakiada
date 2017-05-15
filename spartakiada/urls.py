from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home),
    url(r'add/$', views.add),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'add_new/$', views.add_new),
    url(r'update/(?P<id>\d+)$', views.update),
]