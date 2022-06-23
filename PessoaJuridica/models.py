from django.db import models
class PessoaJuridica (models.Model):
    cnpj = models.CharField(max_length=100)
    razaosocial = models.CharField(max_length=100)
    representantelegal = models.CharField(max_length=100)
    

def __str__(self):
    return self.nome