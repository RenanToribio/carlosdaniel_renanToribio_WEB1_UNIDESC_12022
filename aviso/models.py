from django.db import models

class aviso(models.Model):

    matricula = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    
    
def __str__(self):
    return self.nome
# Create your models here.
