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

def part_list(request, fac_id, sport_id):
    #use = User_f.objects.all()
    #id = use.user
    #print(use,)

    user = User_f.objects.get(faculty_id=fac_id, sport_id=sport_id).user

    part = Participants.objects.filter(user_f_id=user)
    context = {'participants': part,}
    return render(request, 'participants.html', context)

