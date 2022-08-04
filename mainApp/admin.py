from django.contrib import admin
from .models import Caso, Organizacion, PowerUp, Aprobaciones, Contacto, Estado
# Register your models here.

class CasoAdmin(admin.ModelAdmin):
#    list_display = ("id","dueñoCaso","organizacionName","estado","idCaso","tramite","fecha_inicio","fecha_fin" )
     list_display = ("id", "organizacionName")

admin.site.register(Caso, CasoAdmin)

class OrganizacionAdmin(admin.ModelAdmin):
#    list_display = ("id","organizacionUser","nombre","direccion","contacto","email")
     list_display = ("id",)

admin.site.register(Organizacion, OrganizacionAdmin)

class AprobacionesAdmin(admin.ModelAdmin):
#    list_display = ("id","casoEncargado","sociosEncargados","gerenciaFinanciera","pagaduria")
    list_display = ("id", )

admin.site.register(Aprobaciones,AprobacionesAdmin)
admin.site.register(Contacto)
class PowerUpAdmin(admin.ModelAdmin):
   # list_display = ("User","id","estadoWhatsapp","estadoSMS")
    list_display = ("id","name")

admin.site.register(PowerUp,PowerUpAdmin)

admin.site.register(Estado)
