from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.clienteSerializer import ClienteSerializer

class ClienteCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idCliente":request.data["idCliente"],
                     "nombres": request.data["nombres"],
                     "apellidos": request.data["apellidos"],
                     "fechaNacimiento": request.data["fechaNacimiento"],
                     "edad ": request.data["edad "],
                     "telefono": request.data["telefono"],
                     "email": request.data["email"],
                     "direccion": request.data["direccion"],
                     "estado": request.data["estado"]}
        
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)