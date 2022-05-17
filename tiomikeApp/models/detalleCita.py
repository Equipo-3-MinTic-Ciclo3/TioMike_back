from django.db import models

class DetalleCita(models.Model):
    id_detalle_cita = models.AutoField(primary_key=True)
    #id_cita = models.ForeignKey(Cita, related_name='id_cita', on_delete=models.CASCADE)
    #id_producto = models.ForeignKey(Producto, related_name='id_producto', on_delete=models.CASCADE)
    recomendacion = models.TextField('recomendacion')
    estado = models.BooleanField('estado', default=True)
