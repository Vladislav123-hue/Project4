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

class Chat(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    speakingPartnerUsername = models.CharField(max_length=100)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages') #принадлежность класса singlechatinfo в образе коллекции к chat
    content = models.CharField(max_length=100, null=True, blank=True)
    sender = models.CharField(max_length=100, null=True, blank=True)
    receiver = models.CharField(max_length=100, null=True, blank=True)
