from rest_framework import generics
from aComprarApp.models.productosModel import Producto
from aComprarApp.serializers.productoSerializer import productoSerializer

class Catalogo(generics.ListAPIView,generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer

class CatalogoUpdate(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer
