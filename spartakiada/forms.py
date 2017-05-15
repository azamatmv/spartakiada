from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from spartakiada.models import User_f


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=50, required=True)
    faculty = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=True)

class User_fForm(forms.ModelForm):
    class Meta:
        model = User_f
        fields = ('faculty', 'sport_id', 'phone')
        exclude = ()



    '''class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            user.facuty = self.cleaned_data['faculty']

            if commit:
                user.save()
            return user'''

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',

        )



