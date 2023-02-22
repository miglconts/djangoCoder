from django.urls import path
from AppOficina.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    # URLS para ingresar registros
    path('setVidejouego/', setVidejouego, name='videojuego'),
    path('setConsola/', setConsola, name='consola'),
    path('setDesarrollador/', setDesarrollador, name='desarrollador'),
    path('setPersonaje/', setPersonaje, name='personaje'),
    # URLS para buscar registros
    path('buscarVideojuego/', buscarVideojuego, name='buscarVideojuego'),
    path('buscar/', buscar),
    path('registro/', registro, name='registro'),
    # URLS para ver y editar registros
    path('leervideojuegos/', leerVideojuegos, name='leerVideojuegos'),
    path('eliminarVideojuego/<nombreVideojuego>',eliminarVideojuego, name='eliminarVideojuego'),
    path('editarVideojuego/<nombreVideojuego>',updateVidejuego, name='editarVideojuego'),
    path('busqueda/', busqueda, name='busqueda'),
    path('buscarDesarrollador/', buscarDesarrollador, name='buscarDesarrollador'),
    path('buscarDesarrolladores/', buscarDesarrolladores),
    path('leerDesarrolladores/', leerDesarrolladores, name='leerDesarrolladores'),
    path('eliminarDesarrollador/<nombreDesarrollador>',eliminarDesarrollador, name='eliminarDesarrollador'),
    path('editarDesarrollador/<nombreDesarrollador>',updateDesarrollador, name='editarDesarrollador'),
    path('buscarPersonaje/', buscarPersonaje, name='buscarPersonaje'),
    path('buscarPersonajes/', buscarPersonajes),
    path('leerPersonajes/', leerPersonajes, name='leerPersonajes'),
    path('eliminarPersonaje/<nombrePersonaje>',eliminarPersonaje, name='eliminarPersonaje'),
    path('editarPersonaje/<nombrePersonaje>',updatePersonaje, name='editarPersonaje'),
    path('buscarConsola/', buscarConsola, name='buscarConsola'),
    path('buscarConsolas/', buscarConsolas),
    path('leerConsolas/', leerConsolas, name='leerConsolas'),
    path('eliminarConsola/<nombreConsola>',eliminarConsola, name='eliminarConsola'),
    path('editarConsola/<nombreConsola>',updateConsola, name='editarConsola'),
    # URLS pararegistro, edición y creación de usuarios
    path('login/', loginRequest, name="login"),
    path('registrar/', register, name="Signout"),
    path('logout/', LogoutView.as_view(template_name="AppOficina/logout.html"), name="logout"),
    path('editar/', editarUser, name="editarUser"),
    path('avatar/', agregarAvatar, name="avatar"),

]
