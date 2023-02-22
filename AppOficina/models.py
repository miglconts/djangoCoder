from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=40)
    desarrollador = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)

    def __str__(self):
        return f"Videojuego: {self.nombre} | Genero: {self.genero}"


class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    fundada = models.DateField()
    pais = models.CharField(max_length=40)

    def __str__(self):
        return f"Desarrollador: {self.nombre}"


class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    marca = models.CharField(max_length=40)

    def __str__(self):
        return f"Consola: {self.nombre}"


class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    videojuego = models.CharField(max_length=40)
    plataforma = models.CharField(max_length=40)

    def __str__(self):
        return f"Personaje: {self.nombre}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
