"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Apontamentos(models.Model):
    data = models.DateField()
    descricao = models.TextField(max_length=255)
    totalhoras = models.IntegerField()
    aluno = models.ForeignKey(Aluno)