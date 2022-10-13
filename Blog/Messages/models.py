from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse
from Accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.message


    def get_all_messages(id_1, id_2):
        messages = []
        # get messages between the two users, sort them by date(reverse) and add them to the list
        message1 = Message.objects.filter(sender_id=usr_1, receiver_id=usr_2).order_by('-date') 
        # get messages from sender to recipient
        for x in range(len(message1)):
            messages.append(message1[x])
        message2 = Message.objects.filter(sender_id=usr_2, receiver_id=usr_1).order_by('-date') 
        # get messages from recipient to sender
        for x in range(len(message2)):
            messages.append(message2[x])

        # because the function is called when viewing the chat, we'll return all messages as read
        for x in range(len(messages)):
            messages[x].is_read = True
        # sort the messages by date
        messages.sort(key=lambda x: x.date, reverse=False)
        return messages

    # function gets all messages between 'any' two users (requires your pk)
    def get_message_list(u):
        # get all the messages
        m = []  # stores all messages sorted by latest first
        j = []  # stores all usernames from the messages above after removing duplicates
        k = []  # stores the latest message from the sorted usernames above
        for message in Message.objects.all():
            for_you = message.receiver == u  # messages received by the user
            from_you = message.sender == u  # messages sent by the user
            if for_you or from_you:
                m.append(message)
                m.sort(key=lambda x: x.sender.username)  # sort the messages by senders
                m.sort(key=lambda x: x.date, reverse=True)  # sort the messages by date

        # remove duplicates usernames and get single message(latest message) per username(other user) (between you and other user)
        for i in m:
            if i.sender.username not in j or i.receiver.username not in j:
                j.append(i.sender.username)
                j.append(i.receiver.username)
                k.append(i)

        return k