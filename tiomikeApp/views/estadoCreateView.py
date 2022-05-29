from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.estadoSerializaer import EstadoSerializer

class EstadoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = EstadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idEstado":request.data["idEstado"],
                     "descripcion":request.data["descripcion"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)