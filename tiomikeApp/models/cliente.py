from django.db import models
from .usuario import Usuario

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    id_tipo_identificacion = models.ForeignKey(TipoIdentificacion, related_name='tipo_identificacion', on_delete=models.CASCADE)
    nombres = models.CharField('Nombres', max_length = 30)
    Apellidos = models.CharField('Apellidos', max_length = 30)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, related_name='genero', on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, related_name='ciudad', on_delete=models.CASCADE)
    edad = models.IntegerField(default=0)
    telefono = models.IntegerField(default=0)
    email = models.EmailField('Correo', max_length = 30)
    direccion = models.CharField('Direccion', max_length = 30)
    id_barrio = models.ForeignKey(Barrio, related_name='barrio', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)