from django.db import models
from .usuario import Usuario

class Tamano(models.Model):
    id_tamano = models.IntegerField(primary_key=True)
    descripcion = models.CharField('Descripcion', max_length = 30)
    estado = models.BooleanField(default=1)