from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['title', 'subtitle', 'body', 'author', 'date', 'image']