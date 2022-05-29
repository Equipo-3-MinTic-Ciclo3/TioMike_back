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
        fields = ['idCliente', 'cliente_tipo_identificacion', 'nombres', 'apellidos', 'fechaNacimiento', 'cliente_genero', 'cliente_ciudad', 'edad', 'telefono', 'email', 'direccion', 'cliente_barrio', 'estado']
        
    def create(self, validated_data):
        cliente_tipo_identificacionData = validated_data.pop('cliente_tipo_identificacion')
        cliente_generoData = validated_data.pop('cliente_genero')
        cliente_ciudadData = validated_data.pop('cliente_ciudad')
        cliente_barrioData = validated_data.pop('cliente_barrio')
        
        clienteInstance = Cliente.objects.create(**validated_data)
        
        TipoIdentificacion.objects.create(cliente = clienteInstance, **cliente_tipo_identificacionData)
        Genero.objects.create(cliente = clienteInstance, **cliente_generoData) 
        Ciudad.objects.create(cliente = clienteInstance, **cliente_ciudadData)
        Barrio.objects.create(cliente = clienteInstance, **cliente_barrioData)
        return clienteInstance
    
    def to_representation(self, obj):
        cliente = Cliente.objects.get(idCliente=obj.cliente_tipo_identificacion)
        tipoIdentificacion = TipoIdentificacion.objects.get(cliente=obj.cliente_tipo_identificacion)
        genero = Genero.objects.get(cliente=obj.cliente_genero)
        ciudad = Ciudad.objects.get(cliente=obj.cliente_ciudad)
        barrio = Barrio.objects.get(cliente=obj.cliente_barrio)
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
                        'estado':tipoIdentificacion.estado,
                        'genero':{
                            'idGenero':genero.idGenero,
                            'nombreGenero':genero.nombreGenero,
                            'estado':genero.estado,
                            'ciudad':{
                                'idCiudad':ciudad.idCiudad,
                                'nombreCidudad':ciudad.nombreCidudad,
                                'idDepartamento':ciudad.idDepartamento,
                                'barrio':{
                                    'idBarrio':barrio.idBarrio,
                                    'nombreBarrio':barrio.nombreBarrio,
                                    'idCuidad':barrio.idCuidad,
                                    'estado':barrio.idCuidad
                                }
                            }
                        }
                        
                    }                    
        }
        




