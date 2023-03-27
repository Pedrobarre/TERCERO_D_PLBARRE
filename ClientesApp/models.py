from django.db import models
from LoginApp.models import Usuarios
from ClientesApp.choices import sexo
# Create your models here.

class Clientes(models.Model):
    ci = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    estado_Civil = models.CharField(max_length=10,null=True)
    nacionalidad = models.CharField(max_length=50,null=True)
    estado= models.BooleanField('Estado', default= True)
    sexo = models.CharField(max_length=1, choices=sexo, default='1')
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'clientes'