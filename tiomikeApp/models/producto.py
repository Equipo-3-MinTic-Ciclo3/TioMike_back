from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nom_producto = models.CharField('nom_producto', max_length=30, unique=True)
    precio = models.FloatField('precio', default=0)
    id_tipo_producto = models.ForeignKey(TipoProducto, related_name='id_tipo_producto', on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)
