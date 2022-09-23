from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(label='First Name', max_length=100, required=True)
    last_name=forms.CharField(label='Last Name', max_length=100, required=True)
    username=forms.CharField(label='Username',max_length=100, required=True)
    email=forms.EmailField(label='Email',required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

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
        fields = ['name', 'description', 'link', 'image']

class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['image', 'description']