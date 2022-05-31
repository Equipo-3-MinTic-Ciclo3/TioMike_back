from tiomikeApp.models.tipoProducto import TipoProducto
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ['idTipoProducto', 'nombre', 'descripcion', 'estado']
    