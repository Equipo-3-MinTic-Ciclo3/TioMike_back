from rest_framework import serializers

from tiomikeApp.serializers.barrioSerializer import BarrioSerializer
from tiomikeApp.models.barrio import Barrio
from tiomikeApp.models.ciudad import Ciudad
from tiomikeApp.models.departamento import Departamento
class CiudadSerializer(serializers.ModelSerializer):
    barrios = BarrioSerializer(many=True)

    class Meta:
        model = Ciudad
        fields = ['nombreCidudad', 'idDepartamento', 'barrios']

    def create(self, validated_data):
        id = validated_data.prop('idDepartamento')
        barrios_data = validated_data.prop('barrios')
        departamento = Departamento.objects.get(idDepartamento=id)
        ciudad = Ciudad.objects.create(idDepartamento=departamento, **validated_data)
        for barrio_data in barrios_data:
            Barrio.objects.create(idCiudad=ciudad, **barrio_data)
        return ciudad