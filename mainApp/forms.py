from django.forms import ModelForm
from .models import *

class CasoForm(ModelForm):
    class Meta:
        model = Caso
        exclude = ('dueñoCaso','fecha_fin',)