from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MAÑANA VISUAL FORMS TABLAS
# JUEVES REQUEST WHATSAPP - ARCHIVOS -
# VIENRES Mailing - ARCHIVOS
# SABADO DOMINGO INTERFAZ


class Organizacion(models.Model):
    organizacionUser = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    nombre = models.CharField(max_length = 254)
    direccion = models.CharField(max_length = 254)
    contacto_organizacion = models.CharField(max_length = 254) # PROPIO CONTACTO
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre

class Caso(models.Model):
    dueñoCaso = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacionName = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=True) 
    estado = models.BooleanField(default=False)
    idCaso = models.CharField(max_length = 254)
    tramite = models.CharField(max_length = 254) # PDF 
    fecha_inicio = models.DateField(auto_now_add=True)# CUANDO SE NOW()
    fecha_fin = models.DateField(blank=True) # BLANCO HASTA CAMBIAR DE ESTADO CERRADO
    def __str__(self):
        return self.tramite + self.dueñoCaso.username
    
class Contacto(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacionName = models.ForeignKey(Organizacion, on_delete=models.CASCADE,  null=True)  # new
    nombre = models.CharField(max_length = 254)
    apellido = models.CharField(max_length = 254)
    celular = models.CharField(max_length = 254)
    departamento = models.CharField(max_length = 254, null=True)
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre + " " +self.organizacionName.nombre
class PowerUp(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    name = models.CharField(max_length = 254, default="vacio") # Whasap SMS
    url = models.CharField(max_length = 254, default="www.url.com")
    port = models.CharField(max_length = 254, default="8080")
    tipo = models.CharField(max_length = 254, default="get")
   
    def __str__(self):
        return self.User.username

class Aprobaciones(models.Model): #CONTACTO - ESTADO
    class Meta:
        verbose_name_plural = "Aprobaciones"
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    contactoQueAprueba = models.ForeignKey(Contacto, on_delete=models.CASCADE)  # new
    def __str__(self):
        return self.User.username
class Estado(models.Model):
    class Status(models.TextChoices):
        ACTIVO = "1", "ACTIVO"
        INACTIVO = "2", "INACTIVO"
        ABIERTO = "3", "ABIERTO"
        CERRADO = "4", "CERRADO"

    def __str__(self):
        return self.User.username




