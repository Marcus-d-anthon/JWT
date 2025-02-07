from django.db import models

# Create your models here.

class Productos(models.Model):
    Nombre = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=100)
    Cantidad = models.PositiveIntegerField(default=2)
    Marca = models.CharField(max_length=100)
    Fecha_empaquetado = models.DateTimeField(auto_now=True)