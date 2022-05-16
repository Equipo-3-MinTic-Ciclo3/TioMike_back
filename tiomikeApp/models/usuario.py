from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

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
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 30, unique=True)
    password = models.CharField('Password', max_length = 100)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    #id_rol = models.ForeignKey(rol, related_name = 'usuario', on_delete = models.CASCADE)
    estado = models.BooleanField(default=1)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'