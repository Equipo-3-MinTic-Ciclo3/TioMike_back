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
        fields = ['idCliente', 'cliente_tipo_identificacion', 'nombres', 'apellidos', 'fechaNacimiento', 'idGenero', 'idCiudad', 'edad', 'telefono', 'email', 'direccion', 'idBarrio', 'estado']
        
    def create(self, validated_data):
        tipoIdentificacionData = validated_data.pop('cliente_tipo_identificacion')
        clienteInstance = Cliente.objects.create(**validated_data)
        TipoIdentificacion.objects.create(usuario = clienteInstance, **tipoIdentificacionData)
        return clienteInstance
    
    def to_representation(self, obj):
        cliente = Cliente.objects.get(idCliente=obj.cliente_tipo_identificacion)
        tipoIdentificacion = TipoIdentificacion.objects.get(cliente=obj.cliente_tipo_identificacion)
        return {
                    'idCliente':cliente.idCliente, 
                    'nombres':cliente.nombres, 
                    'apellidos':cliente.apellidos, 
                    'fechaNacimiento':cliente.fechaNacimiento,
                    'edad':cliente.edad, 
                    'telefono':cliente.telefono, 
                    'email':cliente.email, 
                    'direccion':cliente.direccion, 
                    'estado':cliente.estado,
                    'tipoIdentificacion': {
                        'idTipoIdentificacion':tipoIdentificacion.idTipoIdentificacion,
                        'nomTipoIdentificacion':tipoIdentificacion.nomTipoIdentificacion,
                        'estado':tipoIdentificacion.estado
                        
                    }                    
        }
        




