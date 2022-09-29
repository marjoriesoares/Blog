from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("", login_form, name="login"),
    path("login/", login_form, name="login"),
    path("logout/",LogoutView.as_view(template_name="Accounts/logout.html"),name="logout"),
    path("profile/<user_id>", profile, name="profile"),
    path("createprofile/<user_id>", createprofile, name="createprofile"),
    path("editprofile/<profile_id>", editprofile, name="editprofile"),
    path("pages/", include("Pages.urls")),
    path("deleteprofile/<user_id>", delete_account , name="deleteaccount"),
]