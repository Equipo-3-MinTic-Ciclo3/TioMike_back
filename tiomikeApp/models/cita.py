from django.db import models
from .mascota import Mascota
from .producto import Producto

class Cita(models.Model):

    idCita = models.AutoField('id_cita', primary_key=True)
    fecha = models.DateTimeField('fecha', auto_now_add=True)
    idMascota = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE)
    idProducto = models.ManyToManyField(Producto, related_name='producto', through="DetalleCita")
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    estado = models.BooleanField('estado', default=True)