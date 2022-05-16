from django.db import models

class Estado(models.Model):
    idEstado = models.AutoField('id_estado',primary_key=True)
    descripcion = models.CharField('descripcion', max_length=30, unique=True)