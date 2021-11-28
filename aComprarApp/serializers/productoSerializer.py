from aComprarApp.models.productosModel import Producto
from rest_framework import serializers
        
class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre', 'caracteristica', 'precio','categoria']
        
        