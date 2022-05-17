from django.db import models
from .ciudad import Ciudad

class Barrio(models.Model):
    idBarrio = models.AutoField('id_barrio', primary_key=True)
    nombreBarrio = models.CharField('nom_barrio', max_length=30, unique=True)
    idCuidad = models.ForeignKey(Ciudad, related_name='barrio_ciudad', on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)
