from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic.list import ListView

class CreateForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['title', 'subtitle', 'content', 'author','image']
