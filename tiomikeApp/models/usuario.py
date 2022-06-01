from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from tiomikeApp.models.rol import Rol

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError('Los usuarios tienen un usuario')
        usuario = self.model(username=username)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, username, password):
        
        usuario = self.create_user(
            username=username,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField('id_usuario', primary_key=True)
    rol = models.ForeignKey(Rol, related_name="id_rol", on_delete=models.CASCADE)
    username = models.CharField('username', max_length = 30, unique=True)
    password = models.CharField('password', max_length = 100)
    nombre = models.CharField('nombre', max_length = 30)
    email = models.EmailField('email', max_length = 100)
    estado = models.BooleanField('estado', default=True)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'