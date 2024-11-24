from django.contrib import admin
from django.urls import path
from base_datos import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación
    path('', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Página de inicio
    path('inicio/', views.inicio, name='inicio'),

    # Rutas para el administrador
    path('admin/programar_agenda/', views.programar_agenda, name='programar_agenda'),
    path('admin/gestionar_inventario/', views.gestionar_inventario, name='gestionar_inventario'),
    path('admin/asignar_herramientas/', views.asignar_herramientas, name='asignar_herramientas'),
    path('admin/generar_reporte_inventario/', views.generar_reporte_inventario, name='generar_reporte_inventario'),
    path('admin/generar_reporte_herramientas/', views.generar_reporte_herramientas, name='generar_reporte_herramientas'),
    path('admin/enviar_notificacion/', views.enviar_notificacion, name='enviar_notificacion'),

    # Rutas para el técnico
    path('tecnico/consulta_agenda/', views.consulta_agenda_tecnico, name='consulta_agenda_tecnico'),
    path('tecnico/registro_servicio/', views.registro_cumplimiento_servicio, name='registro_servicio'),

    # Rutas para el cliente
    path('cliente/confirmacion_servicio/<int:servicio_id>/', views.confirmacion_servicio, name='confirmacion_servicio'),
    path('cliente/consulta_agenda/', views.consulta_agenda_cliente, name='consulta_agenda_cliente'),
]
