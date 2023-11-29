# inventario_patrimonial/models.py

from django.db import models

class Ano(models.Model):
    ano = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.ano)

class Mes(models.Model):
    ano = models.ForeignKey('Ano', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ano.ano} - {self.nome}"
    
class Pagina(models.Model):
    mes = models.ForeignKey('Mes', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    bloco_de_notas = models.TextField()

    def __str__(self):
        return f"{self.mes.ano.ano} - {self.mes.nome} - {self.titulo}"
    