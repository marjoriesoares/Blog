from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Edit email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Edit Name')
    last_name=forms.CharField(label='Edit Surname')

    class Meta:
        model = User
        fields = [ 'email', 'password', 'password_confirmation', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    image= forms.ImageField(label="Choose avatar")

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['name', 'description', 'link', 'email', 'password', 'image']