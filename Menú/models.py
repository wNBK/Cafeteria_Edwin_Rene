from django.db import models


class Producto(models.Model):
    nom_producto = models.CharField(max_length=50)
    precio_producto = models.FloatField()

    def __str__(self):
        return "Nombre del producto: %s Precio: %s" %(self.nom_producto, self.precio_producto)


class CafePreparado(models.Model):
    nom_cafe = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion_cafe = models.CharField(max_length=100)
    tipo_cafe = models.CharField(max_length=100)

    def __str__(self):
        return "Nombre del cafe: %s Descripcion: %s Tipo de cafe: %s" %(self.nom_cafe, self.descripcion_cafe, self.tipo_cafe)

class Comida(models.Model):
    nom_platillo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion_platillo = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)


class Postres(models.Model):
    nom_postre = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion_postre = models.CharField(max_length=100)
    tipo_postre = models.CharField(max_length=100)


class CafeGranel(models.Model):
    nom_CafeGranel = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion_CafeGranel= models.CharField(max_length=100)
    tipo_CafeGranel= models.CharField(max_length=100)


