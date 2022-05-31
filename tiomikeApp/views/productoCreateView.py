from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tiomikeApp.serializers.productoSerializer import ProductoSerializer

class ProductoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"idProducto":request.data["idProducto"],
                     "nomProducto": request.data["nomProducto"],
                     "precio":request.data["precio"],
                     "idTipoProducto":request.data["idTipoProducto"],
                     "estado":request.data["estado"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer._validated_data, status=status.HTTP_201_CREATED)