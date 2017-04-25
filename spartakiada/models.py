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
    faculty = models.ForeignKey(Faculty, null=True)
    sport_id = models.ForeignKey(Sport, null=True)
    phone = models.CharField(max_length=20)
    is_true = models.NullBooleanField(null=True, default=False)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = User_f.objects.create(user=kwargs['instance'])
    def __unicode__(self):
        return(self.user.first_name)
    post_save.connect(create_profile, sender=User)


class Participants(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    pers_num = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=True)
    user_f_id = models.ForeignKey(User, null=True)

    def get_user(self):
        user_f = User_f.objects.get(user=self.user_f_id)
        return u'%s'%(user_f.faculty.faculty_name)

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