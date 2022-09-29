from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Pages(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(default="",max_length=200, unique=True)
    subtitle=models.CharField(max_length=150)
    content = RichTextField()
    def html_content(self):
        return mark_safe(self.content)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image=models.ImageField(upload_to='pages_img',default='default.png',blank=True)

    class Meta:
        ordering=['-date']
    
    @property
    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/pages_img/default.png"

    def __str__(self):
        return f"Author: {self.author} - Title: {self.title} - Date: {self.date}"