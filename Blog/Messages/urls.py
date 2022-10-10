from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MessageListView.as_view(), name='messages_list'),
    path('inbox/<str:username>/', InboxView.as_view(), name='inbox'),
]