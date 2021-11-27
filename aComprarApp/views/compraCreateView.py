from rest_framework import generics

from aComprarApp.models.comprasModel import Compra
from aComprarApp.serializers.comprasSerializer import comprasSerializer
    
class compraCreateView (generics.ListAPIView,generics.CreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = comprasSerializer