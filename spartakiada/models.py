from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Sport(models.Model):
    sport_name = models.CharField(max_length=100)
    def __unicode__(self):
        return (self.sport_name)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100)
    def __unicode__(self):
        return(self.faculty_name)


class User_f(models.Model):
    user = models.OneToOneField(User, null=True)
    faculty_id = models.ForeignKey(Faculty, null=True)
    sport_id = models.ForeignKey(Sport, null=True)
    phone = models.CharField(max_length=20)
    is_true = models.NullBooleanField(null=True, default=False)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = User_f.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


class Participants(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    pers_num = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    depart = models.CharField(max_length=100, null=True)
    user_f_id = models.ManyToManyField(User_f)



class Active_game(models.Model):
    game_name = models.CharField(max_length=200)
    register_date = models.DateTimeField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    otkoruu_jeri = models.TextField()
    sport = models.ManyToManyField(Sport)

    def __unicode__(self):
        return(self.game_name)

class Archive(models.Model):
    name = models.CharField(max_length=200)