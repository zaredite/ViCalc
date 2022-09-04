from ctypes import BigEndianStructure
from tkinter import Place
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Symptoms(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certificate = models.BooleanField()

    def __str__(self):
        return self.user.username

class Masks(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    protection = models.DecimalField(max_digits=10 ,decimal_places=2)

    def __str__(self):
        return self.name

class Vaccines(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    active_cases = models.IntegerField()
    recovered = models.IntegerField()
    new_cases = models.IntegerField()

    def __str__(self):
        return self.name