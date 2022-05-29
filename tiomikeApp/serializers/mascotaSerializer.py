from tiomikeApp.models.mascota import Mascota
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idMascota', 'idCliente', 'nomMascota', 'edadMascota', 'peso', 'idGenero', 'idRaza', 'idTamano', 'historia', 'imagen', 'estado']