from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserEditForm, AvatarForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


def login_form(request):
    if request.method=="POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get("username")
            password=login_form.cleaned_data.get("password")
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'Pages/home.html', {'message':f"Welcome {user}!"})
            else:
                return render(request, 'Accounts/login.html', {"login_form":login_form,'message':'Username or password incorrect'})
        else:
            return render(request, 'Accounts/login.html', {"login_form":login_form, 'message':'Username or password incorrect'})
    else:
        login_form=AuthenticationForm()
        return render(request, 'Accounts/login.html', {"login_form":login_form})

def logout(request):
    return render(request, 'Accounts/logout.html')

def signup(request):
    if request.method=='POST':
        signupform=UserCreationForm(request.POST)
        if signupform.is_valid():
            username=signupform.cleaned_data['username']
            signupform.save()
            return render(request, 'Pages/home.html', {'message':"User sucessfully created"})
    else:
        signupform=UserCreationForm()
    return render(request, 'Accounts/signup.html', {'signupform':signupform})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def editprofile(request):
    return render(request, 'Accounts/editprofile.html')