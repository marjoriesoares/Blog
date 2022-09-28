from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    username = forms.CharField(label="Username", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class UserForm(forms.ModelForm):
    email = forms.EmailField(label="Edit email")
    first_name = forms.CharField(label="Edit Name")
    last_name = forms.CharField(label="Edit Surname")
   
    prefix = "user"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        help_texts = {k: "" for k in fields}


class ProfileForm(forms.ModelForm):
    description = forms.CharField(max_length=500)
    link = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)

    prefix = "profile"

    class Meta:
        model = Profile
        fields = ["description", "link", "image"]
