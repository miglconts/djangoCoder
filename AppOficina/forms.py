from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppOficina.models import Avatar


class DateInput(forms.DateInput):
    input_type = 'date'


class FormVidejuego(forms.Form):
    nombre = forms.CharField()
    lanzamiento = forms.DateField(widget=DateInput)
    plataforma = forms.CharField()
    desarrollador = forms.CharField()
    genero = forms.CharField()


class FormDesarrollador(forms.Form):
    nombre = forms.CharField()
    fundada = forms.DateField(widget=DateInput)
    pais = forms.CharField()


class FormConsola(forms.Form):
    nombre = forms.CharField()
    lanzamiento = forms.DateField(widget=DateInput)
    marca = forms.CharField()


class FormPersonaje(forms.Form):
    nombre = forms.CharField()
    videojuego = forms.CharField()
    plataforma = forms.CharField()


class FormRegistroUser(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'password1', 'password2']
        help_texts = {k: "" for k in fields}


class FormEditarUser(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'password1', 'password2']
        help_texts = {k: "" for k in fields}


class FormAvatar(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['image']
