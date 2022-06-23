from django.db import models
class corretor (models.Model):
    comicao = models.CharField(max_length=100)
    idcorretor = models.CharField(max_length=100)
    

def __str__(self):
    return self.nome
# Create your models here.
