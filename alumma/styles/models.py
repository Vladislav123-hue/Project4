from django.db import models
from django.contrib.auth.models import User

class Style(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(
        blank=True,                    
        null=False                     
    )
    pillow = models.ImageField(default='nameOfPhoto.png', blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class PortfolioWork(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(
        blank=True,                    
        null=False                     
    )
    pillow = models.ImageField(default='nameOfPhoto.png', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chats = models.ManyToManyField('Chat', related_name='participants', blank=True)

class Chat(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='chat_set')
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)