from django.db import models

class TipoProducto(models.Model):
    idTipoProducto = models.AutoField('id_tipo_producto', primary_key=True)
    nombre = models.CharField('nombre', max_length=30, unique=True)
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    estado = models.BooleanField('estado', default=True)
