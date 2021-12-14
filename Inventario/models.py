from django.db import models


class Articulos (models.Model):
    nom_producto = models.CharField(max_length=50)
    precio_producto = models.FloatField()
    descripcion_producto = models.CharField(max_length=100)
    cantidad_existencia = models.CharField(max_length=50)


class PE(models.Model):
    nom_producto = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.FloatField()


class PS(models.Model):
    nom_producto = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.FloatField()


class Proveedores(models.Model):
    nom_proveedor = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

