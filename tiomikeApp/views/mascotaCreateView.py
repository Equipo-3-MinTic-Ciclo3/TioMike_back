from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.mascotaSerializer import MascotaSerializer

class MascotaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MascotaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idMascota":request.data["idMascota"],
                     "idCliente": request.data["idCliente"],
                     "nomMascota": request.data["nomMascota"],
                     "edadMascota": request.data["edadMascota"],
                     "peso": request.data["peso"],
                     "idGenero": request.data["idGenero"],
                     "idRaza": request.data["idRaza"],
                     "idTamano": request.data["idTamano"],
                     "historia": request.data["historia"],
                     "imagen": request.data["imagen"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)