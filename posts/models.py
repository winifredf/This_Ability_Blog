from django.db import models
from datetime import datetime
# Create your models here.
class   Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

