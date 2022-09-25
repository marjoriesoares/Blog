from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserEditForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views import View
from .models import Profile



def login_form(request):
    if request.method=="POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get("username")
            password=login_form.cleaned_data.get("password")
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'Accounts/login.html', {"login_form":login_form,'message':'Username or password incorrect'})
        else:
            return render(request, 'Accounts/login.html', {"login_form":login_form, 'message':'Username or password incorrect'})
    else:
        login_form=AuthenticationForm()
        return render(request, 'Accounts/login.html', {"login_form":login_form})

@login_required
def logout(request):
    return render(request, 'Accounts/logout.html')

def signup(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            email=form.cleaned_data.get("email")
            user=User(username=username, first_name=first_name, last_name=last_name, email=email)
            user.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'Accounts/signup.html', {'form':form})

@login_required
def profile(request):
    profile=Profile.objects.all()
    return render(request, "Accounts/profile.html", {"profile":profile})

@login_required
def editprofile(request, id):
    edit_profile=Profile.objects.get(id=id)
    if request.method=='POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            edit_profile.first_name=data["first_name"]
            edit_profile.last_name=data["last_name"]
            edit_profile.email=data["email"]
            edit_profile.description=data["description"]
            edit_profile.link=data["link"]
            edit_profile.image=data["image"]
            edit_profile.save()
            return render(request, 'Accounts/profile.html')
    else:
        form= Usereditform(initial={"first_name":edit_profile.first_name, 
        "last_name":edit_profile.last_name, "email":edit_profile.email, 
        "description":edit_profile.description,"link":edit_profile.link, 
        "image":edit_profile.image})
        return render(request, "Accounts/editprofile.html")