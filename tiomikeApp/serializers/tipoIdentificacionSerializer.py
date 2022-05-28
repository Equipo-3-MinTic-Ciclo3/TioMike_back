from tiomikeApp.models.tipoIdentificacion import TipoIdentificacion
from rest_framework import serializers

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacion
        fields = []