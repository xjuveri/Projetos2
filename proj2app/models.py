from django.db import models
from django.contrib.auth.models import User
from django import forms

class MeuFormulario(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
# Create your models here.
class ProgressoAluno(models.Model):
    professor = models.CharField(max_length=100)
    atividade = models.CharField(max_length=100)
    data = models.DateField()
