from django.db import models

class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=30, unique=True)
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    estado = models.BooleanField('estado', default=True)
