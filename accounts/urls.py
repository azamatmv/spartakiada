from django.conf.urls import url
from accounts.views import *
from . import views

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'logget$', logget, name='logget'),
    url(r'auth$', auth_view, name='auth_view'),
    url(r'invalid$', invalid, name='invalid'),
    url(r'logout$', logout, name='logout'),
    url(r'register$', register_user, name='register_user'),
    url(r'register_success$', register_success, name='register_success'),
    url(r'del-user$', del_user, name='del-user'),


        ]