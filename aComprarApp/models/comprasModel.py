from django.db import models
from .usuarioModel import User
from .productosModel import Producto

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    total = models.FloatField()
    usuarioFK = models.ForeignKey(User, related_name='compra', on_delete=models.CASCADE)
    productoFK = models.ForeignKey(Producto, related_name='compra', on_delete=models.CASCADE)
    