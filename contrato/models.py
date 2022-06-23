from django.db import models
class contrato (models.Model):
    dadoscliente = models.CharField(max_length=100)
    dadoscorretor = models.CharField(max_length=100)
    descricaoimovel = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    documentacao = models.CharField(max_length=100)
    clausulapenal = models.CharField(max_length=100)

def __str__(self):
    return self.nome
# Create your models here.
