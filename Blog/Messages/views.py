from django.shortcuts import render, redirect
from django.http import HttpResponse

def messages(request):
    return render(request, 'Messages/messages.html')
