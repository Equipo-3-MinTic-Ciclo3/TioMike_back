from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.tipoIdentificacionSerializer import TipoIdentificacionSerializer

class TipoIdentificacionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = TipoIdentificacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idTipoIdentificacion":request.data["idTipoIdentificacion"],
                     "nomTipoIdentificacion": request.data["nomTipoIdentificacion"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)