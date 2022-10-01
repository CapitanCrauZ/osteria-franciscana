import email
from django.db import models

# Create your models here.

class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=40)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=False)
    paternal_lastname = models.CharField(max_length=40, blank=False)
    maternal_lastname = models.CharField(max_length=40, blank=False)
    password = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=None)