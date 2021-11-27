from aComprarApp.models.categoriaModel import Categoria
from rest_framework import serializers

class categoriaSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Categoria
        fields = ['id', 'descripcion']
        

   