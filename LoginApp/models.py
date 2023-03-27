from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=250, null=True)
    correo = models.CharField(max_length=50, null=True)
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=10)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200, blank=True, null=True,
                          default='user.png')
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = 'usuarios'