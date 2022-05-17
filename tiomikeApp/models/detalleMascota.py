from django.db import models
from .mascota import Mascota

class DetalleMascota(models.Model):
    idDetalleMascota= models.AutoField('id_detalle_mascota', primary_key=True)
    idMascota = models.ForeignKey(Mascota, related_name='mascota',on_delete=models.CASCADE)
    fecha = models.DateTimeField('fecha')
    historial = models.CharField('historial', max_length=255)
    