"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
 
class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    
class LocaisProva(models.Model):
    nomeEscola = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
