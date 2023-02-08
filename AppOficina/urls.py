from django.urls import path
from AppOficina.views import *

urlpatterns = [
    path('', home, name='home'),
    path('setVidejouego/', setVidejouego, name='videojuego'),
    path('setConsola/', setConsola, name='consola'),
    path('setDesarrollador/', setDesarrollador, name='desarrollador'),
    path('setPersonaje/', setPersonaje, name='personaje'),
    path('buscarVideojuego/', buscarVideojuego, name='buscarVideojuego'),
    path('buscar/', buscar),
]
