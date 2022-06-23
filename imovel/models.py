from django.db import models
class imovel (models.Model):
    matriculaimovel = models.CharField(max_length=100)
    ruaimovel = models.CharField(max_length=100)
    cepimovel = models.CharField(max_length=100)
    bairroimovel = models.CharField(max_length=100)
    cidadeimovel = models.CharField(max_length=100)
    ufimovel = models.CharField(max_length=100)
    tamanhoimovel = models.CharField(max_length=100)
    comodosimovel = models.CharField(max_length=100)
    garagemimovel = models.CharField(max_length=100)
    valorimovel = models.CharField(max_length=100)
    tipoimovel = models.CharField(max_length=100)
    statusimovel = models.CharField(max_length=100)


def __str__(self):
    return self.nome