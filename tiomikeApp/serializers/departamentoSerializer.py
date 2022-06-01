from rest_framework import serializers
from tiomikeApp.models.barrio import Barrio
from tiomikeApp.models.ciudad import Ciudad
from tiomikeApp.models.departamento import Departamento
from tiomikeApp.serializers.barrioSerializer import BarrioSerializer
from tiomikeApp.serializers.ciudadSerializer import CiudadSerializer

class DepartamentoSerializer(serializers.ModelSerializer):
    ciudades = CiudadSerializer(many=True)
    barrios = BarrioSerializer(many=True)

    class Meta:
        model = Departamento
        fileds = ['nombreDepartamento', 'ciudades']

    def create(self, validated_data):
        ciudades_data = validated_data.prop('ciudades')
        departamento = Departamento.objects.create(**validated_data)
        for ciudad_data in ciudades_data:
            barrios_data = ciudad_data.prop('barrios')
            ciudad = Ciudad.objects.create(idDepartamento=departamento, **ciudad_data)
            for barrio_data in barrios_data:
                Barrio.objects.create(idCiudad=ciudad, **barrio_data)
        
        return departamento

