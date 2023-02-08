from django.db import models

# Create your models here.


class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=40)
    desarrollador = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)


class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    fundada = models.DateField()
    pais = models.CharField(max_length=40)


class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    marca = models.CharField(max_length=40)


class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    videojuego = models.CharField(max_length=40)
    plataforma = models.CharField(max_length=40)
