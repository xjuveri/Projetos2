from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
# Create your models here.
