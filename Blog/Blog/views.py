from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect


def home(request):
    return redirect('/pages')

def messages(request):
    return redirect('/messages')

def accounts(request):
    return redirect('/accounts')