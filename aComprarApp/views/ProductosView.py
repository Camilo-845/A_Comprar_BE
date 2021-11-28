from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
from aComprarApp.models.productosModel import Producto
from aComprarApp.serializers.productoSerializer import productoSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

class ProductosList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer
    permission_classed = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        tokenBackend.decode(token,verify=False)
        return super().get(request, *args, **kwargs)


class ProductoCreate(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer
    permission_classed = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        tokenBackend.decode(token,verify=False)
        return super().post(request, *args, **kwargs)

class ProductoUpdate(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer
    permission_classed = (IsAuthenticated,)
    def put(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        tokenBackend.decode(token,verify=False)
        return super().put(request, *args, **kwargs)

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer
    permission_classed = (IsAuthenticated,)
    def  get(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        tokenBackend.decode(token,verify=False)
        return super().get(request, *args, **kwargs)

