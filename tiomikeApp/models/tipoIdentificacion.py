from django.db import models

class TipoIdentificacion(models.Model):

    idTipoIdentificacion = models.AutoField('id_tipo_identificacion',primary_key=True)
    nomTipoIdentificacion = models.CharField('nom_tipo_identificacion', max_length=30)
    estado = models.BooleanField('estado', default=True)