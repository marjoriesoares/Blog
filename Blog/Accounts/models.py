from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    name=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description=models.CharField(max_length=500)
    link=models.CharField(max_length=200)
    image=models.ImageField(upload_to='avatar', null=False, blank=False)

    def __str__(self):
        return self.name.username