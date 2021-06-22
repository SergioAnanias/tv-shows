from django.db import models
import os


# Create your models here.

class Show(models.Model):
    title= models.CharField(max_length=50)
    network= models.CharField(max_length=20)
    release= models.DateField()
    desc=models.CharField(max_length=255)
    img=models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)