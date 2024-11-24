

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Movimiento, Herramienta, Servicio, Notificacion, Reporte, Agenda
from .forms import ProgramarAgendaForm, RegistroServicioForm, AsignarHerramientaForm, ConfirmacionServicioForm, RetroalimentacionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone

def es_administrador(user):
    return user.is_authenticated and user.rol == 'Administrador'

def es_tecnico(user):
    return user.is_authenticated and user.rol == 'Tecnico'

def es_cliente(user):
    return user.is_authenticated and user.rol == 'Cliente'

@login_required
def inicio(request):
    return render(request, 'inicio.html')

# Administrador

@login_required
@user_passes_test(es_administrador)
def programar_agenda(request):
    if request.method == 'POST':
        form = ProgramarAgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save()
            # Notificar al cliente y al tecnico sobre la nueva agenda
            Notificacion.objects.create(
                usuario=agenda.servicio.cliente,
                tipo='Recordatorio',
                fecha_envio=timezone.now(),
                contenido=f'Su servicio ha sido programado para {agenda.fecha} a las {agenda.hora}.',
                estado='Pendiente'
            )
            Notificacion.objects.create(
                usuario=agenda.servicio.tecnico,
                tipo='Recordatorio',
                fecha_envio=timezone.now(),
                contenido=f'Se ha asignado un nuevo servicio para el {agenda.fecha} a las {agenda.hora}.',
                estado='Pendiente'
            )
            messages.success(request, 'Agenda programada exitosamente y notificaciones enviadas.')
            return redirect('programar_agenda')
        else:
            messages.error(request, 'Error al programar la agenda.')
    else:
        form = ProgramarAgendaForm()
    return render(request, 'admin/programar_agenda.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def gestionar_inventario(request):
    herramientas = Herramienta.objects.all()
    return render(request, 'admin/gestionar_inventario.html', {'herramientas': herramientas})

@login_required
@user_passes_test(es_administrador)
def asignar_herramientas(request):
    if request.method == 'POST':
        form = AsignarHerramientaForm(request.POST)
        if form.is_valid():
            herramienta = form.save(commit=False)
            herramienta.estado = 'En Uso'
            herramienta.save()
            # Registrar el movimiento de herramienta
            Movimiento.objects.create(
                tipo='Egreso',
                herramienta=herramienta,
                cantidad=herramienta.cantidad,
                fecha=timezone.now(),
                responsable=request.user
            )
            messages.success(request, 'Herramienta asignada exitosamente y movimiento registrado.')
            return redirect('asignar_herramientas')
        else:
            messages.error(request, 'Error al asignar la herramienta.')
    else:
        form = AsignarHerramientaForm()
    return render(request, 'admin/asignar_herramientas.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def generar_reporte_inventario(request):
    herramientas = Herramienta.objects.all()
    reporte = Reporte.objects.create(
        tipo='Inventario',
        fecha_creacion=timezone.now(),
        generado_por=request.user,
        contenido='Reporte detallado del estado del inventario.'
    )
    return render(request, 'admin/reporte_inventario.html', {'herramientas': herramientas, 'reporte': reporte})

@login_required
@user_passes_test(es_administrador)
def generar_reporte_herramientas(request):
    movimientos = Movimiento.objects.all()
    reporte = Reporte.objects.create(
        tipo='Utilizacion',
        fecha_creacion=timezone.now(),
        generado_por=request.user,
        contenido='Reporte detallado de la utilizacion de las herramientas.'
    )
    return render(request, 'admin/reporte_herramientas.html', {'movimientos': movimientos, 'reporte': reporte})

@login_required
@user_passes_test(es_administrador)
def enviar_notificacion(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        usuarios = Usuario.objects.filter(is_active=True)
        for usuario in usuarios:
            Notificacion.objects.create(
                usuario=usuario,
                tipo='Alerta',
                fecha_envio=timezone.now(),
                contenido=contenido,
                estado='Pendiente'
            )
        messages.success(request, 'Notificaciones enviadas exitosamente.')
        return redirect('enviar_notificacion')
    return render(request, 'admin/enviar_notificacion.html')

# Tecnico

@login_required
@user_passes_test(es_tecnico)
def consulta_agenda_tecnico(request):
    servicios = Servicio.objects.filter(tecnico=request.user)
    return render(request, 'tecnico/consulta_agenda.html', {'servicios': servicios})

@login_required
@user_passes_test(es_tecnico)
def registro_cumplimiento_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id, tecnico=request.user)
    if request.method == 'POST':
        form = RegistroServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio.estado = 'Completado'
            servicio.save()
            messages.success(request, 'Servicio registrado como completado.')
            return redirect('consulta_agenda_tecnico')
        else:
            messages.error(request, 'Error al registrar el servicio.')
    else:
        form = RegistroServicioForm(instance=servicio)
    return render(request, 'tecnico/registro_servicio.html', {'form': form})

# Cliente

@login_required
@user_passes_test(es_cliente)
def confirmacion_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id, cliente=request.user)
    if request.method == 'POST':
        form = ConfirmacionServicioForm(request.POST, instance=servicio)
        retro_form = RetroalimentacionForm(request.POST)
        if form.is_valid() and retro_form.is_valid():
            servicio.estado = 'Completado'
            servicio.save()
            messages.success(request, 'Servicio confirmado. Gracias por tu retroalimentacion!')
            return redirect('consulta_agenda_cliente')
        else:
            messages.error(request, 'Error al confirmar el servicio.')
    else:
        form = ConfirmacionServicioForm(instance=servicio)
        retro_form = RetroalimentacionForm()
    return render(request, 'cliente/confirmacion_servicio.html', {'form': form, 'retro_form': retro_form})

@login_required
@user_passes_test(es_cliente)
def consulta_agenda_cliente(request):
    servicios = Servicio.objects.filter(cliente=request.user)
    return render(request, 'cliente/consulta_agenda.html', {'servicios': servicios})
