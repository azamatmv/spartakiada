from django.shortcuts import render,  redirect, render_to_response, HttpResponseRedirect
from spartakiada.models import Active_game, Faculty
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from spartakiada.forms import RegistrationForm, EditProfileForm, User_fForm
from django.contrib import messages
from accounts.forms import UserRegistrationForm

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return HttpResponseRedirect('accounts/invalid')


def logget(request):
    fullname = request.user.username
    content = {'full_name': fullname}
    return render_to_response('accounts/logget.html', content)


def invalid(request):
    return render_to_response('accounts/invalid.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register_user(request):
    userform = UserRegistrationForm(request.POST or None)
    user_fform = User_fForm(request.POST or None)
    content = {
        'form1': userform,
        'form2': user_fform,
    }
    if userform.is_valid() and user_fform.is_valid():
        user1 = userform.save()
        profile = user_fform.save(commit=False)
        profile.user1 = user1.id
        profile.save()
      #  userform.save()
      #  uid = userform.id
      #  user_fform.user = uid
      #  user_fform.save()
        return HttpResponseRedirect('accounts/register_success')
    return render(request, 'accounts/register1.html', content)
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #             user = User.objects.create()
    #             user.username = form.cleaned_data['username']
    #             user.password1 = form.cleaned_data['password1']
    #             user.password2 = form.cleaned_data['password2']
    #             user.first_name = form.cleaned_data['first_name']
    #             user.last_name = form.cleaned_data['last_name']
    #             user.email = form.cleaned_data['email']
    #
    #             user.save()
    #
    #            # user_f = User_f.objects.create()
    #             #user.faculty = form.cleaned_data['faculty']
    #             user.phone = form.cleaned_data['phone']
    #             user_f.save()
    #
    #
    #     return HttpResponseRedirect('accounts/register_success')
    #
    # else:
    #     form = RegistrationForm()
    #
    # args = {}
    # args.update(csrf(request))
    # args['form'] = RegistrationForm()
    # return render_to_response('accounts/register.html', args)

def del_user(request):
    try:
        u = User.objects.all()
        u.delete()
        messages.sucess(request, "The user is deleted")
    except:
      messages.error(request, "The user not found")
    return redirect('/')

def register_success(request):
    fullname = request.user.username
    content = {'full_name': fullname}
    return render_to_response('accounts/register_success.html', content)