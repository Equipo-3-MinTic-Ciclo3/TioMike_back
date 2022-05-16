from pyexpat import model
from tkinter import CASCADE
from django.db import models
from .barrio import Barrio

class Proveedor(models.Model):

    idProveedor = models.AutoField('id_proveedor', primary_key=True)
    #idTipoIdentificacion = models.ForeignKey(TipoIdentificacion, related_name="tipo_identificacion", on_delete=CASCADE)
    nombreProveedor = models.CharField('nombre_proveedor', max_length=100)
    email = models.EmailField('email', max_length=100, unique=True)
    idBario = models.ForeignKey(Barrio, related_name='barrio', on_delete=CASCADE)
    telefono = models.CharField('telefono', max_length=10)
    direccion = models.CharField('direccion', max_length=50)
    estado = models.BooleanField('estado', default=True)