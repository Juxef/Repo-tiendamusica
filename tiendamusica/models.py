from django.db import models

# Create your models here.
class Guitarra(models.Model):

    marca=models.CharField(max_length=25)
    color=models.CharField(max_length=14)
    precio = models.IntegerField()

class Amplificador(models.Model):
    marca= models.CharField(max_length=25)
    potencia= models.CharField(max_length=10)
    precio= models.IntegerField()

class Sucursal(models.Model):
    lugar= models.CharField(max_length=40)
    direccion= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.CharField(max_length=30)