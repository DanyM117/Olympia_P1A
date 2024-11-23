"""
URL configuration for AGAN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base_datos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cliente
    path('agenda/consulta/', views.consulta_agenda, name='consulta_agenda'),
    path('servicio/confirmacion/', views.confirmacion_servicio, name='confirmacion_servicio'),
    
    # Técnico
    path('agenda/programar/', views.programar_agenda, name='programar_agenda'),
    path('herramientas/asignar/', views.asignar_herramienta, name='asignar_herramienta'),
    path('servicio/registro/', views.registro_servicio, name='registro_servicio'),

    # Administrador
    path('inventario/gestionar/', views.gestionar_inventario, name='gestionar_inventario'),
    path('reportes/rendimiento/', views.generar_reporte_rendimiento, name='generar_reporte_rendimiento'),
    path('reportes/herramientas/', views.generar_reporte_herramientas, name='generar_reporte_herramientas'),
    path('notificaciones/enviar/', views.enviar_notificacion, name='enviar_notificacion'),
]
