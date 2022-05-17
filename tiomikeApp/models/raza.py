from django.db import models

class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    descripcion = models.CharField('descripcion', max_length=60, unique=True)
    estado = models.BooleanField('estado', default=True)
