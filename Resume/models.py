from django.db import models
from django_quill.fields import QuillField

class Section(models.Model):
    name = models.CharField(max_length=100)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    start = models.DateField(auto_now_add=False, blank=True, null=True)
    end = models.DateField(auto_now=False, blank=True, null=True)
    description = QuillField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + self.section.name
