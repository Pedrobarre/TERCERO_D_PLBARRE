from django.db import models

# Create your models here.
class Distribuiodra(models.Model):
    nombre = models.CharField(max_length=300)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100, null=True)
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'distribuiodra'

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=250)
    estado = models.BooleanField('Estado', default=True)


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'clasificacion'

class Categorias(models.Model):
    nombre = models.CharField(max_length=150)
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria'

class Productos(models.Model):
    codigo = models.CharField(max_length=10, null=True)
    producto = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    precio_compra = models.FloatField(null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='medicamentos/', max_length=200, blank=True, null=True)
    estado = models.BooleanField('Estado', default=True)
    distribuiodra = models.ForeignKey(Distribuiodra, on_delete=models.CASCADE)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto

    class Meta:
        db_table = 'Productos'