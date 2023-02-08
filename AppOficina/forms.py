from django import forms


class FormVidejuego(forms.Form):
    nombre = forms.CharField()
    lanzamiento = forms.DateField()
    plataforma = forms.CharField()
    desarrollador = forms.CharField()
    genero = forms.CharField()


class FormDesarrollador(forms.Form):
    nombre = forms.CharField()
    fundada = forms.DateField()
    plataforma = forms.CharField()


class FormConsola(forms.Form):
    nombre = forms.CharField()
    lanzamiento = forms.DateField()
    marca = forms.CharField()


class FormPersonaje(forms.Form):
    nombre = forms.CharField()
    videojuego = forms.DateField()
    plataforma = forms.CharField()
