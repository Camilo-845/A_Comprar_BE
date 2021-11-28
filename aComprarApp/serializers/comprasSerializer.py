from rest_framework import serializers
from django.db.models import fields
from aComprarApp.models.comprasModel import Compra
from aComprarApp.models.productosModel import Producto
from aComprarApp.models.usuarioModel import User
  
class comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id','fecha','cantidad','total','usuarioFK','productoFK']

    def to_representation(self, obj):
        compra = Compra.objects.get(id=obj.id)
        user = User.objects.get(id=compra.usuarioFK_id)
        producto = Producto.objects.get(id=compra.productoFK_id)
        return {
            'id':compra.id,
            'fecha':compra.fecha,
            'cantidad':compra.cantidad,
            'total':compra.total,
            'usuario':{
                'id':user.id,
                'username':user.username
            },
            'producto':{
                'id':producto.id,
                'nombre':producto.nombre,
                'precio':producto.precio
            }
        }

        

