from django.shortcuts import render
from django.http import HttpResponse
from AppOficina.forms import *
from AppOficina.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Login, Logout, registro de usuarios
def loginRequest(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppOficina/home.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "AppOficina/home.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "AppOficina/home.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppOficina/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = FormRegistroUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppOficina/home.html",  {"mensaje": "Usuario cambiado)"})
    else:
        form = FormRegistroUser()
    return render(request, "AppOficina/registrar.html",  {"form": form})


@login_required
def editarUser(request):
    user = request.user
    if request.method == 'POST':
        form = FormEditarUser(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.email = info['email']
            user.set_password(info['password1'])
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.save()
            return render(request, "AppOficina/home.html",  {"mensaje": f"Usuario "})
    else:
        form = FormEditarUser(initial={
            'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})
    return render(request, "AppOficina/editarPerfil.html",  {"form": form, "user": user})


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = FormAvatar(request.POST, request.FILES)
        if form.is_valid():
            currentUser = User.objects.get(username=request.user)
            avatar = Avatar(user=currentUser, image=form.cleaned_data['image'])
            avatar.save()
            return render(request, "AppOficina/home.html")
    else:
        form = FormAvatar()
    return render(request, "AppOficina/agregarAvatar.html",  {"form": form})

# Páginas de inicio, error y sobre mi


def home(request):
    return render(request, "AppOficina/home.html")


def error404(request, exception):
    return render(request, "AppOficina/404.html")


def error400(request, exception):
    return render(request, "AppOficina/400.html")


def about(request):
    return render(request, "AppOficina/about.html")


def registro(request):
    return render(request, "AppOficina/registro.html")


def busqueda(request):
    return render(request, "AppOficina/busqueda.html")

# Modelos


def setVidejouego(request):
    if request.method == "POST":
        myForm = FormVidejuego(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            videojuego = Videojuego(**info)
            videojuego.save()
            return render(request, "AppOficina/registro.html")
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
            return render(request, "AppOficina/registro.html")
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
            return render(request, "AppOficina/registro.html")
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
            return render(request, "AppOficina/registro.html")
    else:
        myForm = FormPersonaje()
    return render(request, "AppOficina/personajes.html", {"myForm": myForm})


# CRUD Videojuegos
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


@login_required
def leerVideojuegos(request):
    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos": videojuegos}
    return render(request, "AppOficina/leerVideojuego.html", contexto)


def eliminarVideojuego(request, nombreVideojuego):
    videojuego = Videojuego.objects.get(nombre=str(nombreVideojuego))
    videojuego.delete()
    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos": videojuegos}
    return render(request, "AppOficina/leerVideojuego.html", contexto)


def updateVidejuego(request, nombreVideojuego):
    videojuego = Videojuego.objects.get(nombre=str(nombreVideojuego))

    if request.method == "POST":
        myForm = FormVidejuego(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            videojuego.nombre = info['nombre']
            videojuego.lanzamiento = info['lanzamiento']
            videojuego.plataforma = info['plataforma']
            videojuego.desarrollador = info['desarrollador']
            videojuego.genero = info['genero']
            videojuego.save()
            return render(request, "AppOficina/registro.html")
    else:
        myForm = FormVidejuego(initial={
                               'nombre': videojuego.nombre, 'lanzamiento': videojuego.lanzamiento, 'plataforma': videojuego.plataforma, 'desarrollador': videojuego.desarrollador, 'genero': videojuego.genero})
    return render(request, "AppOficina/editarVideojuego.html", {"myForm": myForm, "nombreVideojuego": nombreVideojuego})

# CRUD Desarrolladores


def buscarDesarrollador(request):
    return render(request, "AppOficina/buscarDesarrollador.html")


def buscarDesarrolladores(request):
    if request.GET['desarrollador']:
        consulta = request.GET['desarrollador']
        resultados = Desarrollador.objects.filter(nombre__icontains=consulta)
        return render(request, "AppOficina/resultadoDesarrollador.html", {"consulta": consulta, "resultados": resultados})
    else:
        respuesta = "No datos recopilados"
    return HttpResponse(respuesta)


@login_required
def leerDesarrolladores(request):
    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores": desarrolladores}
    return render(request, "AppOficina/leerDesarrollador.html", contexto)


def eliminarDesarrollador(request, nombreDesarrollador):
    desarrollador = Desarrollador.objects.get(nombre=str(nombreDesarrollador))
    desarrollador.delete()
    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores": desarrolladores}
    return render(request, "AppOficina/leerDesarrollador.html", contexto)


def updateDesarrollador(request, nombreDesarrollador):
    desarrollador = Desarrollador.objects.get(nombre=str(nombreDesarrollador))
    if request.method == "POST":
        myForm = FormDesarrollador(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            desarrollador.nombre = info['nombre']
            desarrollador.fundada = info['fundada']
            desarrollador.pais = info['pais']
            desarrollador.save()
            return render(request, "AppOficina/registro.html")
    else:
        myForm = FormDesarrollador(initial={
            'nombre': desarrollador.nombre, 'fundada': desarrollador.fundada, 'pais': desarrollador.pais})
    return render(request, "AppOficina/editarDesarrollador.html", {"myForm": myForm, "nombreDesarrollador": nombreDesarrollador})


# CRUD Personajes
def buscarPersonaje(request):
    return render(request, "AppOficina/buscarPersonaje.html")


def buscarPersonajes(request):
    if request.GET['personaje']:
        consulta = request.GET['personaje']
        resultados = Personaje.objects.filter(nombre__icontains=consulta)
        return render(request, "AppOficina/resultadoPersonaje.html", {"consulta": consulta, "resultados": resultados})
    else:
        respuesta = "No datos recopilados"
    return HttpResponse(respuesta)


@login_required
def leerPersonajes(request):
    personajes = Personaje.objects.all()
    contexto = {"personajes": personajes}
    return render(request, "AppOficina/leerPersonaje.html", contexto)


def eliminarPersonaje(request, nombrePersonaje):
    personaje = Personaje.objects.get(nombre=str(nombrePersonaje))
    personaje.delete()
    personajes = Personaje.objects.all()
    contexto = {"personajes": personajes}
    return render(request, "AppOficina/leerPersonaje.html", contexto)


def updatePersonaje(request, nombrePersonaje):
    personaje = Personaje.objects.get(nombre=str(nombrePersonaje))
    if request.method == "POST":
        myForm = FormPersonaje(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            personaje.nombre = info['nombre']
            personaje.videojuego = info['videojuego']
            personaje.plataforma = info['plataforma']
            personaje.save()
            return render(request, "AppOficina/registro.html")
    else:
        myForm = FormPersonaje(initial={
            'nombre': personaje.nombre, 'videojuego': personaje.videojuego, 'plataforma': personaje.plataforma})
    return render(request, "AppOficina/editarPersonaje.html", {"myForm": myForm, "nombrePersonaje": nombrePersonaje})

# CRUD Consolas
def buscarConsola(request):
    return render(request, "AppOficina/buscarConsola.html")

def buscarConsolas(request):
    if request.GET['consola']:
        consulta = request.GET['consola']
        resultados = Consola.objects.filter(nombre__icontains=consulta)
        return render(request, "AppOficina/resultadoConsola.html", {"consulta": consulta, "resultados": resultados})
    else:
        respuesta = "No datos recopilados"
    return HttpResponse(respuesta)


@login_required
def leerConsolas(request):
    consolas = Consola.objects.all()
    contexto = {"consolas": consolas}
    return render(request, "AppOficina/leerConsola.html", contexto)


def eliminarConsola(request, nombreConsola):
    consola = Consola.objects.get(nombre=str(nombreConsola))
    consola.delete()
    consolas = Personaje.objects.all()
    contexto = {"consolas": consolas}
    return render(request, "AppOficina/leerConsola.html", contexto)


def updateConsola(request, nombreConsola):
    consola = Consola.objects.get(nombre=str(nombreConsola))
    if request.method == "POST":
        myForm = FormConsola(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            consola.nombre = info['nombre']
            consola.lanzamiento = info['lanzamiento']
            consola.marca = info['marca']
            consola.save()
            return render(request, "AppOficina/registro.html")
    else:
        myForm = FormConsola(initial={
            'nombre': consola.nombre, 'lanzamiento': consola.lanzamiento, 'marca': consola.marca})
    return render(request, "AppOficina/editarConsola.html", {"myForm": myForm, "nombreConsola": nombreConsola})
