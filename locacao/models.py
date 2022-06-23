from django.db import models
class locacao (models.Model):
    datadesocupacao = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    formagarantia = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)


def __str__(self):
    return self.nome