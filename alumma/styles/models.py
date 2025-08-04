from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(
        blank=True,                    
        null=False                     
    )
    pillow = models.ImageField(default='nameOfPhoto.png', blank=True)