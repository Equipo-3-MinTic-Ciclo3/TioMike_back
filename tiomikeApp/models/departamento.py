from django.db import models

class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombreDepartamento = models.CharField('nombre_departamento', max_length=20, unique=True)