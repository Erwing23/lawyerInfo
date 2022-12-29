from django.contrib import admin
from .models import Caso, Organizacion, PowerUp, Aprobaciones, Contacto, File
# Register your models here.

class CasoAdmin(admin.ModelAdmin):
    list_display = ("id","dueñoCaso","organizacionName","status","idCaso","tramite","fecha_inicio","fecha_fin" )
class OrganizacionAdmin(admin.ModelAdmin):
     list_display = ("id","organizacionUser","status","nombre","direccion","contacto_organizacion","email")
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("id","User","organizacionName","status","nombre","apellido","celular","departamento","email" )

class AprobacionesAdmin(admin.ModelAdmin):
    list_display = ("id", "caso","contactoQueAprueba","status")
class PowerUpAdmin(admin.ModelAdmin):
   # list_display = ("User","id","estadoWhatsapp","estadoSMS")
    list_display = ("id","name")
class EstadoAdmin(admin.ModelAdmin):
   # list_display = ("User","id","estadoWhatsapp","estadoSMS")
    list_display = ("id","status")
class FileAdmin(admin.ModelAdmin):
   # list_display = ("User","id","estadoWhatsapp","estadoSMS")
    list_display = ("id","file","fileName","User")

admin.site.register(Caso, CasoAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Aprobaciones,AprobacionesAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(PowerUp,PowerUpAdmin)
admin.site.register(File,FileAdmin)