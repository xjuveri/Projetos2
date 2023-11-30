# relatorio/models.py
from django.db import models

class Relatorio(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    bloco_notas = models.TextField()
    nome_usuario = models.CharField(max_length=100, blank=True, null=True)  # Adicione este campo

    def __str__(self):
        return self.titulo
