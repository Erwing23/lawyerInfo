from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MAÑANA VISUAL FORMS TABLAS
# JUEVES REQUEST WHATSAPP - ARCHIVOS -
# VIENRES Mailing - ARCHIVOS
# SABADO DOMINGO INTERFAZ
"""
class Estado(models.Model):
    class Status(models.TextChoices):
        ACTIVOS =  "1","ACTIVO"
        INACTIVO =  "2","INACTIVO"
        ABIERTO =  "3","ABIERTO"
        CERRADO =  "4","CERRADO"
    status = models.CharField(max_length=25,
        choices=Status.choices,
        default=Status.ACTIVOS )
    def __str__(self):
        return self.status
"""
class Organizacion(models.Model):
    ACTIVO = 'ACT'
    INACTIVO = 'INACT'

    ESTADO_ORGANIZACION = [
        (ACTIVO, 'ACTIVO'),
        (INACTIVO, 'INACTIVO'),
        
    ]
    organizacionUser = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    status = models.CharField(max_length=5, choices=ESTADO_ORGANIZACION, default=ACTIVO,)
    nombre = models.CharField(max_length = 254)
    direccion = models.CharField(max_length = 254)
    contacto_organizacion = models.CharField(max_length = 254) # PROPIO CONTACTO
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre
class Contacto(models.Model):
    ACTIVO = 'ACT'
    INACTIVO = 'INACT'

    ESTADO_CONTACTO = [
        (ACTIVO, 'ACTIVO'),
        (INACTIVO, 'INACTIVO'),
    ]
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacionName = models.ForeignKey(Organizacion, on_delete=models.CASCADE,  null=True)  # new
    status = models.CharField(max_length=5, choices=ESTADO_CONTACTO, default=ACTIVO,)
    nombre = models.CharField(max_length = 254)
    apellido = models.CharField(max_length = 254)
    celular = models.CharField(max_length = 254)
    departamento = models.CharField(max_length = 254, null=True)
    email = models.EmailField(max_length = 254)
    def __str__(self):
        return self.nombre + " " +self.organizacionName.nombre


class Caso(models.Model):
    ACTIVO = 'ACT'
    INACTIVO = 'INACT'
    CERRADO = 'CERR'
    

    ESTADO_APROBACIONES = [
        (ACTIVO, 'ACTIVO'),
        (CERRADO, 'CERRADO'),
        (INACTIVO, 'INACTIVO')     
    ]
    dueñoCaso = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    organizacionName = models.ForeignKey(Organizacion, on_delete=models.CASCADE, null=True) 
    idCaso = models.CharField(max_length = 254)
    status = models.CharField(max_length=5, choices=ESTADO_APROBACIONES, default=ACTIVO,)
    tramite = models.CharField(max_length = 254) # PDF 
    fecha_inicio = models.DateField(auto_now_add=True)# CUANDO SE NOW()
    fecha_fin = models.DateField(null=True,blank=True) # BLANCO HASTA CAMBIAR DE ESTADO CERRADO
    def __str__(self):
        return "Caso: "+self.tramite+" " + self.dueñoCaso.username
class Aprobaciones(models.Model): #CONTACTO - ESTADO
    ABIERTO = 'ABI'
    CERRADO = 'CERR'

    ESTADO_APROBACIONES = [
        (ABIERTO, 'ABIERTO'),
        (CERRADO, 'CERRADO'),
        
    ]
    class Meta:
        verbose_name_plural = "Aprobaciones"
    #User = models.ForeignKey(User, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, null=True)
    contactoQueAprueba = models.ForeignKey(Contacto, on_delete=models.CASCADE)  # new
    status = models.CharField(max_length=5, choices=ESTADO_APROBACIONES, default=ABIERTO,)

    def __str__(self):
        return self.contactoQueAprueba.nombre + " " + self.contactoQueAprueba.departamento
class PowerUp(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    name = models.CharField(max_length = 254, default="vacio") # Whasap SMS
    url = models.CharField(max_length = 254, default="www.url.com")
    port = models.CharField(max_length = 254, default="8080")
    tipo = models.CharField(max_length = 254, default="get")
   
    def __str__(self):
        return self.User.username +" "+ self.name



