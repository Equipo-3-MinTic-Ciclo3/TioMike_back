from rest_framework import serializers
from tiomikeApp.models.barrio import Barrio
from tiomikeApp.models.ciudad import Ciudad

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = ['nombreBarrio', 'estado', 'idCiudad']

    def create(self, validated_data):
        id = validated_data.prop('idCiudad')
        ciudad = Ciudad.objects.get(idCiudad=id)
        barrio = Barrio.objects.create(idCuidad=ciudad, **validated_data)
        return barrio