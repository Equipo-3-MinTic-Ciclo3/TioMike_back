from pyexpat import model
from django.db import models

class Genero(models.Model):
    idGenero = models.AutoField('id_genero',primary_key=True)
    nombreGenero = models.CharField('nombre_genero',max_length=100)
    estado = models.BooleanField('estado', default=True)