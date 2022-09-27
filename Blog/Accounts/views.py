from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  UserRegisterForm, UserForm, ProfileForm
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
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(
                    request,"Accounts/login.html",{"login_form": login_form,"message": "Username or password incorrect"})
        else:
            return render(request,"Accounts/login.html",{"login_form": login_form, "message": "Username or password incorrect"})
    else:
        login_form = AuthenticationForm()
        return render(request, "Accounts/login.html", {"login_form": login_form})


@login_required
def logout(request):
    return render(request, "Accounts/logout.html")


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "Accounts/signup.html", {"form": form})


@login_required
def createprofile(request, user_id):
    create_profile = Profile.objects.get(id=user_id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        user_form = UserForm(request.POST,instance=request.user.profile)
        if form.is_valid() and user_form.is_valid():
            data = form.cleaned_data
            user_data = user_form.cleaned_data

            create_profile.user.first_name = user_data["first_name"]
            create_profile.user.last_name = user_data["last_name"]
            create_profile.user.email = user_data["email"]
            create_profile.user.save()

            create_profile.description = data["description"]
            create_profile.link = data["link"]
            create_profile.image = data["image"]
            create_profile.save()
        else:
            return render(request,"Accounts/createprofile.html",{"user_id": user_id, "form": form, "user_form": user_form})

        return redirect(f"/accounts/profile/{create_profile.user.id}")
    else:
        user_form = UserForm()
        form = ProfileForm()
        return render(request,"Accounts/createprofile.html",{"user_id": user_id, "form": form, "user_form": user_form})




@login_required
def profile(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, "Accounts/profile.html", {"profile": profile, "user": profile.user})


@login_required
def editprofile(request, profile_id):
    edit_profile = Profile.objects.get(id=profile_id)
    if request.method == "POST":
        form = ProfileForm(request.POST, prefix="profile")
        user_form = UserForm(request.POST, prefix="user")
        if form.is_valid() and user_form.is_valid():
            data = form.cleaned_data
            user_data = user_form.cleaned_data

            edit_profile.user.first_name = user_data["first_name"]
            edit_profile.user.last_name = user_data["last_name"]
            edit_profile.user.email = user_data["email"]
            edit_profile.user.save()

            edit_profile.description = data["description"]
            edit_profile.link = data["link"]
            edit_profile.image = data["image"]
            edit_profile.save()
        else:
            return render(request,"Accounts/editprofile.html",{"profile_id": profile_id, "form": form, "user_form": user_form})

        return redirect(f"/accounts/profile/{edit_profile.user.id}")
    else:
        user_form = UserForm(
            initial={"email": edit_profile.user.email,"first_name": edit_profile.user.first_name,"last_name": edit_profile.user.last_name})
        form = ProfileForm(
            initial={"description": edit_profile.description,"link": edit_profile.link,"image": edit_profile.image})
        return render(request,"Accounts/editprofile.html",{"profile_id": profile_id, "form": form, "user_form": user_form})