from django.db import models

class Usuario(models.Model):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Tecnico', 'Tecnico'),
    ]
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=15, choices=ROLES)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=8, choices=ESTADOS)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre


class Herramienta(models.Model):
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('En Uso', 'En Uso'),
        ('En Reparacion', 'En Reparacion'),
    ]

    id_herramienta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=15, choices=ESTADOS)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmado', 'Confirmado'),
        ('Completado', 'Completado'),
    ]

    id_servicio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=12, choices=ESTADOS)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha}"


class Movimiento(models.Model):
    TIPOS = [
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso'),
    ]

    id_movimiento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=7, choices=TIPOS)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.herramienta.nombre}"


class Notificacion(models.Model):
    TIPOS = [
        ('Recordatorio', 'Recordatorio'),
        ('Alerta', 'Alerta'),
    ]
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Enviada', 'Enviada'),
        ('Fallida', 'Fallida'),
    ]

    id_notificacion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=12, choices=TIPOS)
    fecha_envio = models.DateTimeField()
    contenido = models.TextField()
    estado = models.CharField(max_length=9, choices=ESTADOS)

    def __str__(self):
        return f"{self.tipo} - {self.usuario.nombre}"


class Reporte(models.Model):
    TIPOS = [
        ('Inventario', 'Inventario'),
        ('Servicios', 'Servicios'),
    ]

    id_reporte = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    fecha_creacion = models.DateTimeField()
    generado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.tipo} - {self.fecha_creacion}"


class Agenda(models.Model):
    ESTADOS = [
        ('Programada', 'Programada'),
        ('Cancelada', 'Cancelada'),
    ]

    id_agenda = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS)

    def __str__(self):
        return f"{self.fecha} - {self.servicio.cliente.nombre}"
