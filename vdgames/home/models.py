from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Apellido Materno')
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=100, verbose_name='correo')
    mas18=models.BooleanField(default=False)
    id_user=models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    
    class meta:
        verbose_name='Colaborador'
        verbose_name_plural='Colaboradores'

class registro_colaborador(models.Model):
    id_user= models.ForeignKey(Colaboradores,on_delete=models.CASCADE,primary_key=True)
    user = models.CharField(unique=True, max_length=20, verbose_name='usuario')
    contasena = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        return str(self.user)
    
class indie(models.Model):
    nombre=models.CharField(max_length=80)
    categoria=models.CharField(max_length=40)
    image=models.ImageField(upload_to="images", null=True, blank=True)
    descripcion=models.CharField(max_length=500)
    user=models.ForeignKey(registro_colaborador,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)