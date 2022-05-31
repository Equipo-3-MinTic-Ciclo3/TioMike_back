from tiomikeApp.models.detalleCita import DetalleCita
from rest_framework import serializers

class DetalleCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCita
        fields = ['idDetalleCita', 'idCita', 'idProducto', 'recomendacion', 'estado']
    