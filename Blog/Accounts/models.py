from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description=models.CharField(max_length=500)
    link=models.CharField(max_length=200)
    image=models.ImageField(default='default.png',upload_to='avatar')
    email=models.ForeignKey(User,  default='user.email', on_delete=models.CASCADE, related_name='+')
    first_name=models.ForeignKey(User, default='user.first_name', on_delete=models.CASCADE, related_name='+')
    last_name=models.ForeignKey(User, default='user.last_name', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.user.username+" "+self.user.email