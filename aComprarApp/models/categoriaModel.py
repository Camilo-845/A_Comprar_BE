from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField('Descripción', max_length=20)