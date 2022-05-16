from django.db import models

class Mascota(models.Model):

    idMascota = models.AutoField('id_mascota',primary_key=True)
    #idCliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.CASCADE)
    nomMascota = models.CharField('nom_mascota', max_length=30)
    edadMascota = models.IntegerField('edad_mascota', default=0)
    peso = models.FloatField('peso', default=0)
    #idGenero = models.ForeignKey(Genero, related_name='genero', on_delete=models.CASCADE)
    #idRaza = models.ForeignKey(raza, related_name='raza', on_delete=models.CASCADE)
    #idTamano = models.ForeignKey(Tamano, related_name='tamano', on_delete=models.CASCADE)
    historia = models.CharField('historia', max_length=300)
    imagen = models.CharField('imagen', max_length=255)
    estado = models.BooleanField('estado', default=True)