from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class PerfilGestor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos específicos do perfil do gestor aqui

class PerfilEducador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilGestor.objects.create(user=instance)
        PerfilEducador.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfilgestor.save()
    instance.perfileducador.save()