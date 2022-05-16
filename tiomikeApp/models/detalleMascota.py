from pyexpat import model
from tkinter import CASCADE
from django.db import models
from .mascota import Mascota

class DetalleMascota(models.Model):
    idDetalleMascota= models.AutoField('id_detallemas', primary_key=True)
    idMascota = models.ForeignKey(Mascota, related_name='mascota',on_delete=CASCADE)
    fecha = models.DateTimeField('fecha')
    historial = models.CharField('historial', max_length=255)
    