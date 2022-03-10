from django.db import models

# Create your models here.
class Foto(models.Model):
    foto=models.CharField(max_length=30)
# modelo para la entidad producto
class Producto(models.Model):
    foto=models.ForeignKey(Foto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

class UsuariosTabla(models.Model):
    username=models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2= models.CharField(max_length=30)


