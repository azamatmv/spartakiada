from django.conf.urls import include, url
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from profiles.views import *


urlpatterns = [

    url(r'^$', view_profile, name='profile'),
    url(r'^edit$', edit_profile, name='edit_profile'),
    url(r'^change_password$', change_password, name='change_password'),
    url(r'^password_reset$', password_reset, name='password_reset'),
    url(r'^password_reset/done$', password_reset_done, name='password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete$', password_reset_complete, name='password_reset_complete'),




]