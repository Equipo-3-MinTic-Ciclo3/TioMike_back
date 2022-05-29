from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from tiomikeApp.models.tipoIdentificacion import TipoIdentificacion
from tiomikeApp.serializers.tipoIdentificacionSerializer import TipoIdentificacionSerializer

class TipoIdentificacionDetailView(generics.RetrieveAPIView):
    queryset = TipoIdentificacion.objects.all()
    serializer_class = TipoIdentificacionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['idTipoIdentificacion'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)