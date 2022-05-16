from pyexpat import model
from tkinter import CASCADE
from django.db import models
from .cliente import Cliente
from django.utils import timezone

class Factura(models.Model):
    idFactura = models.AutoField('id_factura', primary_key=True)
    fecha = models.DateTimeField('fecha',  default=timezone.now)
    idCliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=CASCADE)
    estado = models.BooleanField('estado',default=True)
