from django.db import models

class Estacao(models.Model):
    nome_entidade = models.CharField(max_length=100)
    num_servico = models.CharField(max_length=100)
    num_estacao = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tecnologia = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=100)
    azimute = models.CharField(max_length=100)
    altura_antena = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_entidade
