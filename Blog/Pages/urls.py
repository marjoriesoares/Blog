from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', PagesListView.as_view(), name='home'),
    path('about/', about , name='about'),
    path('create/', create, name='create'),
    path('edit/<slug:slug>', editpage, name='editpage'),
    path('<slug:slug>/', page_detail , name='page_detail'),
    path('delete/<slug:slug>/', deletepage , name='deletepage')
]
