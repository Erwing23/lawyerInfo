from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Caso(models.Model):
    dueñoCaso = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacion = models.CharField(max_length = 254)
    estado = models.BooleanField(default=False)
    idCaso = models.CharField(max_length = 254)
    tramite = models.CharField(max_length = 254)

class Organizacion(models.Model):
    organizacionUser = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    nombre = models.CharField(max_length = 254)
    direccion = models.CharField(max_length = 254)
    contacto = models.CharField(max_length = 254)
    email = models.EmailField(max_length = 254)

