from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolio')
    image = models.ImageField(upload_to='Portfolio/images/')
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    show = models.BooleanField(default=True)

    class Meta():
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.title