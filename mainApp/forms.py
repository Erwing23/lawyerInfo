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
    class Meta:
        model = Contacto
        exclude = ('dueñoCaso','fecha_fin',)
class OrganizacionForm(ModelForm):
    class Meta:
        model = Contacto
        exclude = ('dueñoCaso','fecha_fin',)