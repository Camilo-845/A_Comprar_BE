from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings

from aComprarApp.models.comprasModel import Compra
from aComprarApp.serializers.comprasSerializer import comprasSerializer

from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
    
class CompraCreate (generics.CreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = comprasSerializer
    permission_classed = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)

class CompraList(generics.ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = comprasSerializer
    permission_classed = (IsAuthenticated,)
    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Compra.objects.filter(usuarioFK_id = self.kwargs['user'])
        return queryset