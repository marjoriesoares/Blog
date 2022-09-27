from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home , name='home'),
    path('pageslist/', PagesListView.as_view(), name='pages_list'),
    path('about/', about , name='about'),
    path('create/', create, name='create'),
    path('edit/<page_id>', editpage, name='editpage')
]
