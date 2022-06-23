from django.db import models
class boleto(models.Model):

    codigocliente = models.CharField(max_length=100)
    nomecliente = models.CharField(max_length=100)
    
    
def __str__(self):
    return self.nome
# Create your models here.
