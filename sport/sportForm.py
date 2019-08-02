from django import forms
from django.contrib.auth.models import User
from sport.models import Userprofile


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=3, strip=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')
