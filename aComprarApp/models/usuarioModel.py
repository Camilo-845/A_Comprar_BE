from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, nombre, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        user = self.model(nombre=nombre)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
        nombre=nombre,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    cedula = models.BigIntegerField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 15)
    apellido = models.CharField('Apellido', max_length=20)
    password = models.CharField('Contraseña', max_length = 256)
    email = models.EmailField('Email',unique=True, max_length = 100)
    telefono = models.BigIntegerField("Telefono")
    fnacimiento = models.DateField("FechaNacimiento")
    pais = models.CharField("Pais", max_length=10)
    departamento = models.CharField("Departamento", max_length=12)
    ciudad = models.CharField("Ciudad", max_length=12)
    direccion = models.CharField("Dirección", max_length=30)
     
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'cedula'
