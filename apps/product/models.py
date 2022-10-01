from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.category

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    image = models.FileField(upload_to='media/%Y/%m/%d/', default=None)
    base_price = models.IntegerField(blank=False)
    offer_price = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)