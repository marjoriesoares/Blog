from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from Accounts.models import *
from .models import *
from .forms import *


class MessageListView(LoginRequiredMixin, ListView):
    queryset = Message.objects.all().order_by("date")
    model = Message
    template_name = "Messages/messages_list.html"

    def get_context_data(self, **Kwargs):
        context = super().get_context_data(**Kwargs)
        user = User.objects.get(pk=self.request.user.pk)
        messages = Message.get_message_list(user)

        other_users = []

        for i in range(len(messages)):
            if messages[i].sender != user:
                other_users.append(messages[i].sender)
            else:
                other_users.append(messages[i].receiver)

        context["messages"] = messages
        context["other_users"] = other_users
        context["you"] = user
        return context


class InboxView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "Messages/inbox.html"
    login_url = "/login/"
    queryset = User.objects.all()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(User, username__iexact=UserName)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.pk)
        other_user = User.objects.get(username__iexact=self.kwargs.get("username"))
        messages = Message.get_message_list(user)

        other_users = []
        for i in range(len(messages)):
            if messages[i].sender != user:
                other_users.append(messages[i].sender)
            else:
                other_users.append(messages[i].receiver)

        sender = other_user
        receiver = user

        context["messages"] = Message.get_all_messages(sender, receiver)
        context["messages_list"] = messages
        context["other_person"] = other_user
        context["you"] = user
        context["other_users"] = other_users

        return context

    def post(self, request, username):
        sender = User.objects.get(pk=request.POST.get("you"))
        receiver = User.objects.get(pk=request.POST.get("recipient"))
        message = request.POST.get("message")
        if request.user.is_authenticated:
            if request.method == "POST":
                if message:
                    Message.objects.create(
                        sender=sender, receiver=receiver, message=message
                    )
                    return redirect("inbox", username=receiver.username)
                else:
                    return render(request, "Messages/messages_list.html")