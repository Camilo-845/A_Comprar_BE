from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15 , unique=True)
    nombre = models.CharField('Nombre', max_length=20)
    apellido = models.CharField('Apellido', max_length=20)
    password = models.CharField('Contraseña', max_length = 256)
    email = models.EmailField('Email',unique=True, max_length = 100)
    telefono = models.BigIntegerField("Telefono")
     
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'
