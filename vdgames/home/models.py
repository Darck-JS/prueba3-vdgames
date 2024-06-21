from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    user = models.CharField(unique=True, max_length=20)
    contasena = models.CharField(max_length=12, null=False, blank=False)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=100)