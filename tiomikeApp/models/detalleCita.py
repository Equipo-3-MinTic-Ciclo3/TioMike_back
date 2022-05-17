from django.db import models
from .cita import Cita
from .producto import Producto

class DetalleCita(models.Model):
    idDetalleCita = models.AutoField('id_detalle_cita', primary_key=True)
    idCita = models.ForeignKey(Cita, related_name='detalle_cita_cita', on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, related_name='detalle_cita_producto', on_delete=models.CASCADE)
    recomendacion = models.TextField('recomendacion')
    estado = models.BooleanField('estado', default=True)
