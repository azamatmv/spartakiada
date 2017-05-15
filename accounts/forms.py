#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='сыр сөзүңүздү кайталаңыз')
    password = forms.CharField(widget=forms.PasswordInput(), label='сыр сөз')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirmation')
        exclude = ()
