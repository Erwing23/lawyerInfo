from django.contrib import admin
from .models import Caso, Organizacion, PowerUp, Aprobaciones, Contacto
# Register your models here.

class CasoAdmin(admin.ModelAdmin):
    list_display = ("id","dueñoCaso","organizacionName","estado","idCaso","tramite","fecha_inicio","fecha_fin" )
admin.site.register(Caso, CasoAdmin)

class OrganizacionAdmin(admin.ModelAdmin):
    list_display = ("id","organizacionUser","nombre","direccion","contacto","email")
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Aprobaciones)
admin.site.register(Contacto)
class PowerUpAdmin(admin.ModelAdmin):
    list_display = ("User","id","estadoWhatsapp","estadoSMS")

admin.site.register(PowerUp,PowerUpAdmin)
