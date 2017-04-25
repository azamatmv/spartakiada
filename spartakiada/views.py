import datetime
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from spartakiada.models import Active_game, Faculty, Participants, User_f
from django.contrib.auth.models import User
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
    students = Participants.objects.filter(user_f_id=request.user.id)
    st_user = User_f.objects.all()
    # username=User_f.objects.last()
    # department=User_f.objects.first()
    # print(department)
    context = {'students': students, 'user':request.user, 'st_user': st_user}
    return render(request, 'add.html', context)

def add_new(request):
   # print(request.POST)
   # args = {'user': request.user}
    participants = Participants(name=request.POST['namew'], surname=request.POST['surname'],
                                pers_num=request.POST['num'], phone=request.POST['phone'],
                                user_f_id=request.user)

    # participants.department = User_f.objects.get(id=request.user).faculty
    #print(User_f.objects.get(id=request.user).faculty)
    participants.save()
    return redirect('/add/')



