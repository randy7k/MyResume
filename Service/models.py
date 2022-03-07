from django.db import models

class Service(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name