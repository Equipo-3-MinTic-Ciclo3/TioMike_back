from tiomikeApp.models.genero import Genero
from rest_framework import serializers

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = []