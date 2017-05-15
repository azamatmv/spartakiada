from django.shortcuts import render
from spartakiada.models import Sport, Faculty ,Participants, User_f
from django.contrib.auth.models import User


# Create your views here.
def sports_list(request):
    sports = Sport.objects.all()
    context = {'sports':sports}
    return render(request, 'about_sports.html', context)

def fac_list(request):
    fac = Faculty.objects.all()
    context = {'fac': fac}
    return render(request, 'about_fac.html', context)

def part_list(request):
    #use = User_f.objects.all()
    #id = use.user
    #print(use,)
    part = Participants.objects.all()
    context = { 'participants': part  }
    return render(request, 'participants.html', context)

