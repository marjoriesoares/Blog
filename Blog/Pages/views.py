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

class PagesCreateView(CreateView):
    template_name= 'Pages/createpage.html'
    form_class= PagesForm
    queryset= Pages.objects.all()
    sucess_url='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        



