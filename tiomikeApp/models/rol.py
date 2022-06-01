from django.db import models

class Rol(models.Model):
    idRol = models.AutoField('id_rol', primary_key=True)        
    nombre = models.CharField('nombre', unique=True, max_length = 30)
    estado = models.BooleanField('estado', default=True)