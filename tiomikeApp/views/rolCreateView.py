from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.rolSerializer import RolSerializer

class RolCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = RolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idRol":request.data["idRol"],
                     "nombre": request.data["nombre"],
                     "estado":request.data["estado"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)