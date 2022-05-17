from django.db import models
from .mascota import Mascota

class Cita(models.Model):

    idCita = models.AutoField('id_cita', primary_key=True)
    fecha = models.DateTimeField('fecha', auto_now_add=True)
    idMascota = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE)
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    idDetalleCita = models.ForeignKey(DetalleCita, related_name='detalle_cita', on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)