from django.db.models import fields
from rest_framework import serializers
from aComprarApp.models.usuarioModel import User



class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cedula', 'nombre', 'apellido', 'password', 'email', 'telefono', 'fnacimiento', 'pais', 'departamento',
                  'ciudad', 'direccion']
     
     
   