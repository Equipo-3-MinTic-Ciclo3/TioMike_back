from rest_framework import serializers
from tiomikeApp.models.usuario import Usuario
from tiomikeApp.models.rol import Rol
from tiomikeApp.serializers.rolSerializer import RolSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'nombre', 'email', 'rol', 'estado']
        
    def create(self, validated_data):
        rolData = validated_data.pop('rol')
        userInstance = Usuario.objects.create(**validated_data)
        Rol.objects.create(usuario = userInstance, **rolData)
        return userInstance
    
    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id)
        rol = Rol.objects.get(usuario=obj.id)
        return {
                    'id':usuario.id,
                    'username':usuario.username,
                    'nombre':usuario.nombre,
                    'email':usuario.email,
                    'estado':usuario.estado,
                    'rol': {
                        'id':rol.id,
                        'nombre':rol.nombre,
                        'estado':rol.estado
                        
                    }                    
        }
        