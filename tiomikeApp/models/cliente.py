from django.db import models
from .tipoIdentificacion import TipoIdentificacion
from .genero import Genero
from .ciudad import Ciudad
from .barrio import Barrio

class Cliente(models.Model):
    idCliente = models.AutoField('id_cliente', primary_key=True)
    idTipoIdentificacion = models.ForeignKey(TipoIdentificacion, related_name='cliente_tipo_identificacion', on_delete=models.CASCADE)
    nombres = models.CharField('nombres', max_length = 30)
    apellidos = models.CharField('apellidos', max_length = 30)
    fechaNacimiento = models.DateField()
    idGenero = models.ForeignKey(Genero, related_name='cliente_genero', on_delete=models.CASCADE)
    idCiudad = models.ForeignKey(Ciudad, related_name='cliente_ciudad', on_delete=models.CASCADE)
    edad = models.IntegerField(default=0)
    telefono = models.IntegerField(default=0)
    email = models.EmailField('correo', max_length = 30)
    direccion = models.CharField('direccion', max_length = 30)
    idBarrio = models.ForeignKey(Barrio, related_name='cliente_barrio', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)