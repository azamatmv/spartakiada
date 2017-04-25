from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from spartakiada.models import Active_game, Faculty
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

from spartakiada.forms import (
    RegistrationForm,
    EditProfileForm

)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from spartakiada.models import User_f


# Create your views here.
@login_required
def view_profile(request):
    user_f = User_f.objects.all()
    args = {'user': request.user, 'user_f': user_f}
    return render(request, 'profile.html', args)

def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'profile.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)

