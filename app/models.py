from django.db import models
import os, re
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    def validator(self, post_Data):
        errors={}
        now=datetime.now()

        text_regex= re.compile(r'^[A-Za-z0-9]+$')
        if len(post_Data['title']) < 2:
            errors['title'] = "Title must have at least 2 characters, just letters and numbers allow"
            if not text_regex.match(post_Data['title']):    
                errors['title'] = "Just letters and numbers allow"
        if Show.objects.filter(title=post_Data['title']):
            errors['title'] = "This show already exists"
        if post_Data['release'] == '':
            errors['release'] = "You must add a date"
        if post_Data['release'] != '':
            release=datetime.strptime(post_Data['release'], '%Y-%m-%d')
            if release >= now:
                errors['release']= "The date is not valid"
        if len(post_Data['network']) < 3:
            errors['network'] = "It must have at least 3 characters"
        if post_Data['desc'] != '':
            if len(post_Data['desc']) < 10:
                errors['desc'] = "It must have at least 10 characters, be creative"
        return errors

class Show(models.Model):
    title= models.CharField(max_length=50)
    network= models.CharField(max_length=20)
    release= models.DateField()
    desc=models.CharField(max_length=255)
    img=models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()
    def __str__(self):
        return f"{self.title}"
    def __repr__(self):
        return f"{self.title}"