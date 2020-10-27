from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'userna',
            'nim',
            'prodi',
            'email',
            'password'
        ]



