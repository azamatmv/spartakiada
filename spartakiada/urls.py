from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home),
    url(r'add/$', views.add),
    url(r'add_new/$', views.add_new),
]