from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', PagesListView.as_view(), name='home'),
    path('about/', about , name='about'),
    path('create/', create, name='create'),
    path('edit/<page_id>', editpage, name='editpage'),
    path('<slug:slug>/', PageDetail.as_view(), name='page_detail')
]
