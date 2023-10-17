from django.db import models

# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)