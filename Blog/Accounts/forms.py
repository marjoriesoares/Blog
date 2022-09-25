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
    first_name=forms.CharField(label='Edit Name')
    last_name=forms.CharField(label='Edit Surname')
    description=models.CharField(max_length=500)
    link=models.CharField(max_length=200)
    image=models.ImageField(default='default.png',upload_to='avatar')


    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email', 'description','link','image']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    image= forms.ImageField(label="Choose avatar")

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['user', 'description', 'link', 'image']