from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import *
from .forms import *
from Accounts.models import Profile
from Accounts.views import *


def home(request):
    return render(request, 'Pages/home.html')

def about(request):
    return render(request, 'Pages/about.html')

class PagesListView(ListView):
    model= Pages
    template_name="Pages/pages_list.htmml"

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            subtitle = form.cleaned_data.get("subtitle")
            content = form.cleaned_data.get("content")
            author = form.cleaned_data.get("author")
            image = form.cleaned_data.get("image")
            post= Pages(title=title,subtitle=subtitle,content=content,author=author,image=image)
            post.save()
            return redirect("pages_list")
    else:
        form = CreateForm()
    return render(request, "Pages/createpage.html", {"form": form})
        



