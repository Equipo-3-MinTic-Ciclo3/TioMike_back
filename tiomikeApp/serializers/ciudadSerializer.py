from tiomikeApp.models.ciudad import Ciudad
from rest_framework import serializers

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = []