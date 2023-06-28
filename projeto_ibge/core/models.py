from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    cor = models.CharField(max_length=2)
    idade = models.IntegerField()
    genero = models.CharField(max_length=1)
    salario = models.DecimalField(max_digits=10, decimal_places=2)