from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib.auth.models import User

class Pages(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=150)
    body=models.CharField(max_length=12000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    image=models.ImageField(upload_to='pages_img',default='default.png',blank=True)

    def __str__(self):
        return f"Author: {self.author} - Title: {self.title} - Date: {self.date}"
