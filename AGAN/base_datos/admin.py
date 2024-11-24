from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Herramienta, Servicio, Movimiento, Notificacion, Reporte, Agenda

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informacion Adicional', {'fields': ('rol', 'telefono', 'direccion')}),
    )

admin.site.register(Usuario, CustomUserAdmin)
#admin.site.register(Cliente)
admin.site.register(Herramienta)
admin.site.register(Servicio)
admin.site.register(Movimiento)
admin.site.register(Notificacion)
admin.site.register(Reporte)
admin.site.register(Agenda)
