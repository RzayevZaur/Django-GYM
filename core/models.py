from django.db import models

# Create your models here.
class Index(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
    

class Haqqında(models.Model):
    haqqimizda = models.TextField(max_length=30)
    taskbar = models.CharField(max_length=30)

    def __str__(self):
        return self.haqqimizda


    

    


    
