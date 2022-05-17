from django.db import models
from .tipoProducto import TipoProducto

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nomProducto = models.CharField('nom_producto', max_length=30, unique=True)
    precio = models.FloatField('precio', default=0)
    idTipoProducto = models.ForeignKey(TipoProducto, related_name='id_tipo_producto', on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)
