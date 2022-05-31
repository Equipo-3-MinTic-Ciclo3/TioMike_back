from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.detalleCitaSerializer import DetalleCitaSerializer

class DetalleCitaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = DetalleCitaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idDetalleCita":request.data["idDetalleCita"],
                     "idCita": request.data["idCita"],
                     "idProducto": request.data["idProducto"],
                     "recomendacion": request.data["recomendacion"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)