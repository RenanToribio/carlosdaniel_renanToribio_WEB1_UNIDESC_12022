from django.db import models
class Notafiscal (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datadela = models.CharField(max_length=100)
    codigodela = models.CharField(max_length=100)

def __str__(self):
    return self.nome