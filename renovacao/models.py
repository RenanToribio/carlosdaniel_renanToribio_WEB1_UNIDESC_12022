from django.db import models
class renovacao (models.Model):
    datadesocupacao = models.CharField(max_length=100)
    datarenovacao = models.CharField(max_length=100)
    cartorio = models.CharField(max_length=100)
    

def __str__(self):
    return self.nome