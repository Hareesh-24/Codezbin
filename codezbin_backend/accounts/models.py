# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)  # for clean URLs
    content = models.TextField()  # Course content

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)
    achievements = models.TextField(blank=True)
    payments = models.TextField(blank=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True)
    def __str__(self):
        return self.user.username
