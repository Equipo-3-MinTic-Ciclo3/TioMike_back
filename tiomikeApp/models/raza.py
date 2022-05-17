from django.db import models

class Raza(models.Model):
    idRaza = models.AutoField('id_raza', rimary_key=True)
    descripcion = models.CharField('descripcion', max_length=60, unique=True)
    estado = models.BooleanField('estado', default=True)
