from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.CharField(max_length=500)
    link = models.URLField(default='')
    image = models.ImageField(default="avatar/default.png", upload_to="avatar", blank=True)

    def __str__(self):
        return self.user.username + " " + self.user.email