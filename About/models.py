from django.db import models
from django_quill.fields import QuillField
from django.core.validators import MinValueValidator, MaxValueValidator

class AboutMe(models.Model):
    image = models.ImageField(upload_to='about_me')
    title = models.CharField(max_length=200)
    description = QuillField()
    show_counts = models.BooleanField(default=True)

    skills_title = models.CharField(max_length=200, default="Skills")
    show_skills = models.BooleanField(default=True)
    interests_title = models.CharField(max_length=200, default="Tnterests")
    show_interests = models.BooleanField(default=True)
    testimonials_title = models.CharField(max_length=200, default="Testimonials")
    show_testimonials = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.title

class Count(models.Model):
    icon = models.CharField(max_length=200)
    count = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' (' + str(self.count) + ')'

class Skill(models.Model):
    name        = models.CharField(max_length=25, blank=False, null=False)
    percentage  = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name + " " + str(self.percentage) + "%"

class Interest(models.Model):
    icon = models.CharField(max_length=200)
    color = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials', blank=True, null=True)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name