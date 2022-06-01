from urllib import response
from rest_framework import status, views
from django.conf import settings
from tiomikeApp.models.barrio import Barrio

from tiomikeApp.serializers.barrioSerializer import BarrioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BarrioCreateView(views.APIView):
    serializer_class = BarrioSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        barrios = Barrio.objects.all()
        serializer = BarrioSerializer(barrios, many=True)
        return response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BarrioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "idBarrio":request.data["idBarrio"],
            "nombreBarrio":request.data["nombreBarrio"],
            "idCuidad":request.data["idCuidad"],
            "estado":request.data["estado"]
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)