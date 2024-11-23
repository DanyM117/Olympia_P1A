from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Usuario, Cliente, Herramienta, Servicio, Notificacion, Reporte, Agenda

# Cliente
def consulta_agenda(request):
    servicios = Agenda.objects.all()
    return render(request, 'cliente/consulta_agenda.html', {'servicios': servicios})

def confirmacion_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)
    if request.method == "POST":
        servicio.estado = "Completado"
        servicio.save()
        return redirect('consulta_agenda')
    return render(request, 'cliente/confirmacion_servicio.html', {'servicio': servicio})

# Técnico
def programar_agenda(request):
    if request.method == "POST":
        # Lógica para programar agenda
        pass
    return render(request, 'tecnico/programar_agenda.html')

def asignar_herramienta(request):
    herramientas = Herramienta.objects.filter(estado="Disponible")
    return render(request, 'tecnico/asignar_herramienta.html', {'herramientas': herramientas})

def registro_servicio(request):
    if request.method == "POST":
        # Lógica para registrar cumplimiento
        pass
    return render(request, 'tecnico/registro_servicio.html')

# Administrador
def gestionar_inventario(request):
    herramientas = Herramienta.objects.all()
    return render(request, 'admin/gestionar_inventario.html', {'herramientas': herramientas})

def generar_reporte_rendimiento(request):
    reportes = Reporte.objects.filter(tipo="Rendimiento")
    return render(request, 'admin/reporte_rendimiento.html', {'reportes': reportes})

def generar_reporte_herramientas(request):
    reportes = Reporte.objects.filter(tipo="Utilización")
    return render(request, 'admin/reporte_herramientas.html', {'reportes': reportes})

def enviar_notificacion(request):
    if request.method == "POST":
        # Lógica para enviar notificaciones
        pass
    return render(request, 'admin/enviar_notificacion.html')
