from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organizacion(models.Model):
    organizacionUser = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    nombre = models.CharField(max_length = 254)
    direccion = models.CharField(max_length = 254)
    contacto = models.CharField(max_length = 254)
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre

class Caso(models.Model):
    dueñoCaso = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacionName = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=True) 
    estado = models.BooleanField(default=False)
    idCaso = models.CharField(max_length = 254)
    tramite = models.CharField(max_length = 254)
    fecha_inicio = models.DateField(blank=True)
    fecha_fin = models.DateField(blank=True)
    def __str__(self):
        return self.tramite
    
class Contacto(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    nombre = models.CharField(max_length = 254)
    apellido = models.CharField(max_length = 254)
    celular = models.CharField(max_length = 254)
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre
class PowerUp(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    estadoWhatsapp = models.BooleanField(default=False)
    estadoSMS = models.BooleanField(default=False)
    def __str__(self):
        return self.User.username

class Aprobaciones(models.Model):
    casoEncargado = models.ForeignKey(Caso, on_delete=models.CASCADE)  # new
    sociosEncargados = models.BooleanField(default=False)
    gerenciaFinanciera = models.BooleanField(default=False)
    pagaduria = models.BooleanField(default=False)
    def __str__(self):
        return self.casoEncargado.dueñoCaso.username



