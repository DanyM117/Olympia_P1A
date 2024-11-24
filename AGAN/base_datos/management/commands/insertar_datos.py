from django.core.management.base import BaseCommand
from base_datos.models import Usuario, Cliente, Herramienta, Servicio, Movimiento, Notificacion, Reporte, Agenda
from django.utils import timezone

class Command(BaseCommand):
    help = 'Inserta datos de prueba en la base de datos'

    def handle(self, *args, **kwargs):
        # Crear Usuarios
        admin = Usuario.objects.create_user(
            username='admin',
            password='adminpass',
            rol='Administrador',
            email='admin@agan.com'
        )
        tecnico = Usuario.objects.create_user(
            username='tecnico',
            password='tecnicopass',
            rol='Tecnico',
            email='tecnico@agan.com'
        )
        cliente1 = Usuario.objects.create_user(
            username='cliente1',
            password='cliente1pass',
            rol='Cliente',
            email='cliente1@ejemplo.com'
        )
        cliente2 = Usuario.objects.create_user(
            username='cliente2',
            password='cliente2pass',
            rol='Cliente',
            email='cliente2@ejemplo.com'
        )

        # Crear Herramientas
        herramienta1 = Herramienta.objects.create(
            nombre="Taladro",
            estado="Disponible",
            cantidad=10,
            ubicacion="Almacen A"
        )
        herramienta2 = Herramienta.objects.create(
            nombre="Martillo",
            estado="Disponible",
            cantidad=15,
            ubicacion="Almacen B"
        )

        # Crear Servicios
        servicio1 = Servicio.objects.create(
            cliente=cliente1,
            tecnico=tecnico,
            fecha=timezone.now().date(),
            duracion=2,
            estado="Pendiente",
            descripcion="Revision de sistema electrico"
        )
        servicio2 = Servicio.objects.create(
            cliente=cliente2,
            tecnico=tecnico,
            fecha=timezone.now().date(),
            duracion=4,
            estado="Confirmado",
            descripcion="Instalacion de aire acondicionado"
        )

        # Crear Agenda
        agenda1 = Agenda.objects.create(
            servicio=servicio1,
            fecha=servicio1.fecha,
            hora="10:00:00",
            estado="Programada"
        )
        agenda2 = Agenda.objects.create(
            servicio=servicio2,
            fecha=servicio2.fecha,
            hora="14:00:00",
            estado="Programada"
        )

        self.stdout.write(self.style.SUCCESS("Registros creados exitosamente."))
