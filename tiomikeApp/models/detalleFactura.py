from django.db import models

class DetalleFactura(models.Model):

    idDetalleFactura = models.AutoField(primary_key=True)
    #idProducto = models.ForeignKey(Producto, related_name='producto', on_delete=models.CASCADE)
    #idFactura = models.ForeignKey(Factura, related_name='factura', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad', default=0)
    precioVenta = models.FloatField('precio_venta', default=0)
    estado = models.BooleanField('estado', default=True)