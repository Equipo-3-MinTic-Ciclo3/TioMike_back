from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.tamanoSerializer import TamanoSerializer

class TamanoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = TamanoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idTamano":request.data["idTamano"],
                     "descripcion": request.data["descripcion"],
                     "estado":request.data["descripcion"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)





