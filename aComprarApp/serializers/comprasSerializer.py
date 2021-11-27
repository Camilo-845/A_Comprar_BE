from rest_framework import serializers
from django.db.models import fields
from aComprarApp.models.comprasModel import Compra
  
class comprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id','fecha','total','usuarioFK','productoFK']

        

