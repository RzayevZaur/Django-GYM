from django.db import models
# from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils import timezone


class Paraqraf(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs):
         if not self.created_at:
            self.created_at = timezone.now()
         super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    img = models.ImageField(upload_to= 'img',null=False, blank = True,  verbose_name=" img")
    slug = models.SlugField(null=True, blank=True, unique=True,db_index=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         if not self.created_at:
            self.created_at = timezone.now()
         super().save(*args, **kwargs)