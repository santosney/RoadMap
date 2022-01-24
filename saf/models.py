from dataclasses import field
from pyexpat import model
from turtle import st
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    
    def __SignUp__(self):
        return self.user_name
    
    def __SignIn__(self):
        return self.first_name
    
    
class Publication(models.Model):
    data = models.CharField(default="votre description du jours", max_length=120)
    date_publication = models.DateTimeField(verbose_name="date de publication",  auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __Create__(self):
        return self.data
    
    def __update__(self):
        return self.data
    
    def __delete__(self):
        return self.data