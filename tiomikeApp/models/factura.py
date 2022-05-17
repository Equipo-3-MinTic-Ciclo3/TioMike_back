from django.db import models

from .producto import Producto
from .cliente import Cliente
from django.utils import timezone

class Factura(models.Model):
    idFactura = models.AutoField('id_factura', primary_key=True)
    fecha = models.DateTimeField('fecha',  default=timezone.now)
    idCliente = models.ForeignKey(Cliente, related_name='factura_cliente', on_delete=models.CASCADE)
    idProducto = models.ManyToManyField(Producto, related_name='factura_producto', through='DetalleFactura')
    estado = models.BooleanField('estado',default=True)
