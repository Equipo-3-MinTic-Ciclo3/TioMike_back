from django.db import models
from tiomikeApp.models.usuario import Usuario

class Rol(models.Model):
    id = models.IntegerField('id', primary_key=True)    
    id= models.ForeignKey(Usuario, related_name = 'rol', on_delete = models.CASCADE)
    nombre = models.CharField('nombre', max_length = 30)
    estado = models.BooleanField('estado', default=True)