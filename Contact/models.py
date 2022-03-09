from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=2000)
    sended_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' (' + self.email + ') at: ' + self.sended_on.strftime("%m/%d/%Y, %H:%M:%S")
