from webbrowser import BackgroundBrowser
from django.db import models

class Header(models.Model):
    background = models.ImageField(upload_to='Home/backgrounds', blank=True, null=True)
    logo = models.ImageField(upload_to='Home/logos', blank=True, null=True)
    name = models.CharField(max_length=100, default="John Doe")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name