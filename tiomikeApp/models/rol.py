from django.db import models

class Rol(models.Model):
    idRol = models.IntegerField('id_rol', primary_key=True)
    nombre = models.CharField('nombre', max_length = 30)
    estado = models.BooleanField('estado', default=True)