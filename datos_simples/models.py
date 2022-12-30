from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Curso(models.Model):
  nombre = models.CharField(max_length=200, unique=True)

  def __str__(self):
    return self.nombre

class Carrera(models.Model):
  nombre = models.CharField(max_length=200, unique=True)

  def __str__(self):
    return self.nombre

class DistribucionCargaAcademica(models.Model):
  archivo = models.FileField(upload_to='distribucion_academica/')

  def __str__(self):
    return self.archivo.name

class UserManager(BaseUserManager):
  def create_user(self, nombre, password=None):
    """Creates and saves a User with the given email and password."""
    if not nombre:
      raise ValueError('Users must have an name.')

    user = self.model(nombre=nombre)

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_staffuser(self, nombre, password):
    user = self.create_user(nombre, password)
    user.staff = True
    user.save(using=self._db)
    return user

  def create_superuser(self, nombre, password):
    user = self.create_user(nombre, password)
    user.staff = True
    user.admin = True
    user.save(using=self._db)
    return user

class Docente(AbstractBaseUser):
  nombre = models.CharField(
    verbose_name='Nombre Completo',
    max_length=255,
    unique=True
  )
  staff = models.BooleanField(default=False) # a admin user, non super-user
  admin = models.BooleanField(default=False) # a superuser

  # el password ya viene implementado

  USERNAME_FIELD = 'nombre' # django identifica de esta forma al usuario
  REQUIRED_FIELDS = [] # email y password son requeridos por defecto

  def get_full_name(self):
    return self.nombre

  def get_short_name(self):
    return self.nombre

  def __str__(self) -> str:
    return self.nombre

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.staff

  @property
  def is_admin(self):
    return self.admin

  objects = UserManager()