from django.db.models import fields
from rest_framework import serializers
from aComprarApp.models.usuarioModel import User



class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password', 'nombre', 'apellido', 'email','telefono']
     
     
   