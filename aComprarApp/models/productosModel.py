from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=25)
    caracteristica = models.TextField('Caracteristica')
    precio = models.FloatField('precio')
    categoria = models.TextField('categoria',max_length=25 )