from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.tipoProductoSerializer import TipoProductoSerializer

class TipoProductoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = TipoProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idTipoProducto":request.data["idDetalleCita"],
                     "nombre": request.data["idCita"],
                     "descripcion": request.data["descripcion"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)