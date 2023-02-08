from django.shortcuts import render
from django.http import HttpResponse
from AppOficina.forms import *
from AppOficina.models import *

# Create your views here.


def home(request):
    return render(request, "AppOficina/home.html")


def setVidejouego(request):
    if request.method == "POST":
        myForm = FormVidejuego(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            videojuego = Videojuego(**info)
            videojuego.save()
            return render(request, "AppOficina/home.html")
    else:
        myForm = FormVidejuego()
    return render(request, "AppOficina/videojuego.html", {"myForm": myForm})


def setDesarrollador(request):
    if request.method == "POST":
        myForm = FormDesarrollador(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            desarrollador = Desarrollador(**info)
            desarrollador.save()
            return render(request, "AppOficina/home.html")
    else:
        myForm = FormDesarrollador()
    return render(request, "AppOficina/desarrollador.html", {"myForm": myForm})


def setConsola(request):
    if request.method == "POST":
        myForm = FormConsola(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            consola = Consola(**info)
            consola.save()
            return render(request, "AppOficina/home.html")
    else:
        myForm = FormConsola()
    return render(request, "AppOficina/consola.html", {"myForm": myForm})


def setPersonaje(request):
    if request.method == "POST":
        myForm = FormPersonaje(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            personaje = Personaje(**info)
            personaje.save()
            return render(request, "AppOficina/home.html")
    else:
        myForm = FormPersonaje()
    return render(request, "AppOficina/personajes.html", {"myForm": myForm})


def buscarVideojuego(request):

    return render(request, "AppOficina/buscarVideojuego.html")


def buscar(request):

    if request.GET['videojuego']:
        consulta = request.GET['videojuego']
        resultados = Videojuego.objects.filter(nombre__icontains=consulta)
        return render(request, "AppOficina/resultadoVideojuego.html", {"consulta": consulta, "resultados": resultados})
    else:
        respuesta = "No datos recopilados"

    return HttpResponse(respuesta)
