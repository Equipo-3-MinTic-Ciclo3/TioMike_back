from tiomikeApp.models.estado import Estado
from rest_framework import serializers

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['idEstado', 'descripcion']