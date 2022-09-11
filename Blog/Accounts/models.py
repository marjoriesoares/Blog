from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    link=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    image=models.ImageField(upload_to='avatar', null=False, blank=False)

    def __str__(self):
        return f"Name: {self.name} - Email {self.email}"