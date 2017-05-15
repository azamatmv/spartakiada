from django.conf.urls import url, include
from about_faculties.views import *

urlpatterns = [

    url(r'^$', fac_list, name='fac_list'),
    url(r'^sports/$', sports_list, name='sports_list'),
    url(r'^sports/participants/$', part_list, name='sports_list'),
   # url(r'^list/(?P<fac_id>[0-9]+)/(?P<sport_id>[0-9]+)/$', sports_list,  name='sports_list'),


]