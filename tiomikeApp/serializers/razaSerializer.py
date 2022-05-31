from tiomikeApp.models.raza import Raza
from rest_framework import serializers

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ['idRaza','descripcion','estado']
    