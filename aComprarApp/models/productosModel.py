from django.db import models
from .categoriaModel import Categoria

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=25)
    caracteristica = models.TextField('Caracteristica')
    precio = models.FloatField('precio')
    foto = models.ImageField()
    categoriaFK = models.ForeignKey(Categoria, related_name='producto', on_delete=models.CASCADE)
    