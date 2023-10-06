from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    pais = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    
    

