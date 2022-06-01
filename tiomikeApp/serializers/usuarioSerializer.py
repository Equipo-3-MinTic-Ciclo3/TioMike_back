from rest_framework import serializers
from tiomikeApp.models.usuario import Usuario
from tiomikeApp.models.rol import Rol
from tiomikeApp.serializers.rolSerializer import RolSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer()

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password',
                  'nombre', 'email', 'rol', 'estado']

    def create(self, validated_data):
        rol_data = validated_data.pop('rol')
        rol = Rol.objects.create(**rol_data)
        userInstance = Usuario.objects.create(rol=rol, **validated_data)
        return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id)
        rol = Rol.objects.get(idRol=usuario.rol.id)
        return {
            'id': usuario.id,
            'username': usuario.username,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'estado': usuario.estado,
            'rol': {
                'idRol': rol.idRol,
                'nombre': rol.nombre,
                'estado': rol.estado
            }
        }
