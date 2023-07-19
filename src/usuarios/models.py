from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='foto_perfil', null=True, blank=True)