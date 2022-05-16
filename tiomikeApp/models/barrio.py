from tkinter import CASCADE
from django.db import models

class Barrio(models.Model):
    idBarrio = models.AutoField(primary_key=True)
    nombreBarrio = models.CharField('nom_barrio', max_length=30, unique=True)
    #idCuidad = models.ForeignKey(Ciudad, related_name='ciudad', on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)
