import datetime
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from spartakiada.models import Active_game, Faculty
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import (
    RegistrationForm,
    EditProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
    active_games = Active_game.objects.filter(date_end__gte=datetime.datetime.now())
    fullname = request.user.username
    content = {'games': active_games,'full_name': fullname}
    return render(request, 'home.html', content)







def add(request):
    return render(request, 'add.html')



