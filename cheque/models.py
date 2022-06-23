from django.db import models
class cheque(models.Model):

    financeira = models.CharField(max_length=100)
    nomecliente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    dataabertura = models.CharField(max_length=100)

def __str__(self):
    return self.nome
# Create your models here.
