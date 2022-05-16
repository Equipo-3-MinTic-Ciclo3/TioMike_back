from django.db import models
from .usuario import Usuario

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 30)
    estado = models.BooleanField(default=True)