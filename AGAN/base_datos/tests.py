from django.test import TestCase
from .models import Usuario, Notificacion

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="Admin", rol="Administrador", correo="admin@ejemplo.com", estado="Activo")
        Usuario.objects.create(nombre="Tecnico", rol="T�cnico", correo="tecnico@ejemplo.com", estado="Activo")

    def test_usuario_roles(self):
        admin = Usuario.objects.get(nombre="Admin")
        tecnico = Usuario.objects.get(nombre="Tecnico")
        self.assertEqual(admin.rol, "Administrador")
        self.assertEqual(tecnico.rol, "T�cnico")

class NotificacionTestCase(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create(nombre="Usuario", rol="Administrador", correo="user@ejemplo.com", estado="Activo")
        Notificacion.objects.create(usuario=usuario, contenido="Prueba de notificaci�n", estado="Pendiente")

    def test_notificacion_creacion(self):
        notificacion = Notificacion.objects.get(contenido="Prueba de notificaci�n")
        self.assertEqual(notificacion.estado, "Pendiente")