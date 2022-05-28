from rest_framework import serializers
from tiomikeApp.models.cliente import Cliente
from tiomikeApp.models.tipoIdentificacion import TipoIdentificacion
from tiomikeApp.models.ciudad import Ciudad
from tiomikeApp.models.genero import Genero
from tiomikeApp.models.barrio import Barrio
from tiomikeApp.serializers.tipoIdentificacionSerializer import TipoIdentificacionSerializer
from tiomikeApp.serializers.ciudadSerializer import CiudadSerializer
from tiomikeApp.serializers.generoSerializer import GeneroSerializer
from tiomikeApp.serializers.barrioSerializer import BarrioSerializer

class ClienteSerializer(serializers.ModelSerializer):
    tipoIdentificacion = TipoIdentificacionSerializer()
    class Meta:
        model = Cliente
        fields = ['id', 'username', 'password', 'nombre', 'email', 'rol', 'estado']




