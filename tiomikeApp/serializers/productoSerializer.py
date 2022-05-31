from tiomikeApp.models.producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nomProducto','precio','idTipoProducto','estado']
    