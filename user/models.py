from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    major = models.CharField(max_length=60)
    grade = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    writing = models.BooleanField(default=False)
    movie = models.BooleanField(default=False)
    camera = models.BooleanField(default=False)
    photoshop = models.BooleanField(default=False)
    xuanchuan = models.BooleanField(default=False)
    caiwu = models.BooleanField(default=False)
    wailian = models.BooleanField(default=False)
    xueyuan = models.BooleanField(default=False)
    fileUrl = models.CharField(max_length=100)
    firstNoon = models.BooleanField(default=False)
    firstNight = models.BooleanField(default=False)
    secondNoon = models.BooleanField(default=False)
    secondNight = models.BooleanField(default=False)
    userStatus = models.BooleanField(default=False)
