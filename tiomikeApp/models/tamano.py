from django.db import models
from .usuario import Usuario

class Tamano(models.Model):
    idTamano = models.AutoField('id_tamano', primary_key=True)
    descripcion = models.CharField('descripcion', max_length = 30)
    estado = models.BooleanField('estado', default=True)