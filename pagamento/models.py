from django.db import models
class pagamento (models.Model):
    valor = models.CharField(max_length=100)
    forma = models.CharField(max_length=100)
    parcelas = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=100)
    conta = models.CharField(max_length=100)


def __str__(self):
    return self.nome