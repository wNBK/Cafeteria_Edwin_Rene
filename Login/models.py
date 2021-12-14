from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    contr = models.CharField(max_length=50)
    email = models.EmailField()





