from tiomikeApp.models.tamano import Tamano
from rest_framework import serializers

class TamanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamano
        fields = ['descripcion', 'estado']
    