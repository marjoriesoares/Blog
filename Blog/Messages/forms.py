from django import forms
from django.forms import ModelForm
from .models import *

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    message = forms.CharField(max_length=200)

    class Meta:
        model = Message
        fields = ["receiver", "message"]