from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.citaSerializer import CitaSerializer

class CitaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CitaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idCita":request.data["idCita"],
                     "fecha": request.data["fecha"],
                     "idMascota": request.data["idMascota"],
                     "idProducto": request.data["idProducto"],
                     "descripcion": request.data["descripcion"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)