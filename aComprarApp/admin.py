from django.contrib import admin

# Register your models here.
from .models.usuarioModel import User
from .models.comprasModel import Compra
from .models.productosModel import Producto

admin.site.register(User)
admin.site.register(Compra)
admin.site.register(Producto)

