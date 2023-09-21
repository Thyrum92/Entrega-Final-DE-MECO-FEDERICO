from django.db import models

# Create your models here.

class Personal(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    mail = models.CharField(max_length=70)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=15)
    cp = models.IntegerField()
    numero_contacto = models.IntegerField()
    nombre_emergencia = models.CharField(max_length=60)
    apellido_emergencia = models.CharField(max_length=60)
    vinculo = models.CharField(max_length=15)
    numero_contacto_emergencia = models.IntegerField()
    sector = models.CharField(max_length=15)
    permisos = models.CharField(max_length=15)

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=10)