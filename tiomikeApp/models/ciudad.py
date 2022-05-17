from django.db import models
from .departamento import Departamento

class Ciudad(models.Model):
    idCiudad = models.AutoField('id_cidudad', primary_key=True)
    nombreCidudad = models.CharField('nombre_ciudad',max_length=30)
    idDepartamento = models.ForeignKey(Departamento, related_name='departamento', on_delete=models.CASCADE)
    