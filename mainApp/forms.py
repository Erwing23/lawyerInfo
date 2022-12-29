from cProfile import label
from dataclasses import fields
from django.forms import ModelForm
from django import forms

from .models import *

class CasoForm(ModelForm):
    class Meta:
        organizacionName = forms.CharField(label = 'Nombre de la Organización')
        model = Caso
        fields = ('organizacionName','tramite',)
        widgets = {
            'organizacionName': forms.Select(attrs={'class': 'form-control','placeholder':'Nombre de Organización'}),
            'tramite': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del trámite'}),
         }
        

class ContactoForm(ModelForm):
    #
    class Meta:
        model = Contacto
        exclude = ('User','status')
        widgets = {
                'organizacionName': forms.Select(attrs={'class': 'form-control','placeholder':'Nombre de Organización'}),
                'nombre': forms.TextInput( attrs={'class': 'form-control','placeholder':'Nombre de la organización'}),
                'apellido': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dirección'}),
                'celular': forms.TextInput(attrs={'class': 'form-control','placeholder':'Contacto'}),
                'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo'}),
                'departamento': forms.TextInput(attrs={'class': 'form-control','placeholder':'Departamento'}),
         }

class OrganizacionForm(ModelForm):
    class Meta:
        model = Organizacion
        exclude = ('organizacionUser','status',)
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de la organización'}),
                'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dirección'}),
                'contacto_organizacion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Contacto'}),
                'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo'}),
         }
class FileForm(ModelForm):
    class Meta:
        model = File
        exclude = ('User',"caso")
        widgets = {
                'fileName': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del Archivo'}),
                'file': forms.FileInput(attrs={'class': 'form-control','placeholder':'Nombre del Archivo'}),

         }