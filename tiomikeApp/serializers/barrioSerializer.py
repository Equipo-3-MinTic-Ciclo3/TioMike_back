from tiomikeApp.models.barrio import Barrio
from rest_framework import serializers

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = []