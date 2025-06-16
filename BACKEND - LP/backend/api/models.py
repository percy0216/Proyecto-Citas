from django.db import models
from django.utils import timezone  # Sirve para manejar fechas y horas automáticamente
from django.contrib.auth.models import AbstractUser, BaseUserManager



# -------------------
# GESTOR DE USUARIOS 
# -------------------


class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        # Crea un usuario común con nombre de usuario, correo y contraseña
        if not email:
            raise ValueError('Correo es obligatorio')
        email = self.normalize_email(email)  # Normaliza el correo (ej: todo minúsculas)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        # Crea un superusuario (acceso total al sistema/admin)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El campo staff debe ser True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El campo superusuario debe ser True')

        return self.create_user(username, email, password, **extra_fields)

# -------------------------------------
# MODELO DE USUARIO PERSONALIZADO
# -------------------------------------
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True)

    # AbstractUser ya tiene el campo correo definido como email, por lo que no es necesario volver a definirlo.
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=[
            ('paciente', 'Paciente'),
            ('medico', 'Médico'),
            ('admin', 'Administrador')
        ],
        default='paciente'  # Por defecto, cualquier nuevo usuario es un paciente
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Método que permite actualizar varios campos del perfil del usuario
    def actualizar_perfil(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

# -------------------------------------
# MODELO DE PACIENTE
# -------------------------------------
class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)  # Relación uno a uno con Usuario
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()

    def solicitar_cita(self, especialidad, fecha, hora):
        # El paciente puede solicitar una cita médica
        return Cita.objects.create(
            fecha=fecha,
            hora=hora,
            especialidad=especialidad,
            paciente=self
        )

    def consultar_historial(self):
        # Retorna todas las entradas de su historial médico
        return self.historialmedico_set.all()

    def __str__(self):
        return self.usuario.nombre

# -------------------------------------
# MODELO DE ESPECIALIDAD MÉDICA
# -------------------------------------
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# -------------------------------------
# MODELO DE MÉDICO
# -------------------------------------
class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    horario_libre = models.TextField(blank=True, null=True)

    def ver_citas_asignadas(self):
        return self.cita_set.all()

    def registrar_atencion(self, cita, observaciones):
        # Cuando el médico atiende una cita, se guarda un historial
        HistorialMedico.objects.create(paciente=cita.paciente, observaciones=observaciones)
        cita.estado = 'atendida'
        cita.save()

    def __str__(self):
        return self.usuario.nombre

# -------------------------------------
# MODELO DE CITA MÉDICA
# -------------------------------------
class Cita(models.Model):
    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('atendida', 'Atendida'),
    ]

    fecha = models.DateField()
    hora = models.TimeField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='pendiente')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def cancelar(self):
        self.estado = 'cancelada'
        self.save()

    def confirmar(self):
        self.estado = 'confirmada'
        self.save()

# -------------------------------------
# MODELO DE REGISTRO DE VISITAS
# -------------------------------------
class RegistroVisitas(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    hora_ingreso = models.DateTimeField(default=timezone.now)
    motivo = models.TextField()
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='visitas')



# -------------------------------------
# MODELO DE ADMINISTRADOR
# -------------------------------------


class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def crear_usuario(self, **datos_usuario):
        # Crea un nuevo usuario (paciente, médico o admin)
        return Usuario.objects.create(**datos_usuario)

    def modificar_cita(self, cita, **nuevos_datos):
        # Modifica los datos de una cita
        for key, value in nuevos_datos.items():
            setattr(cita, key, value)
        cita.save()

    def eliminar_usuario(self, usuario_id):
        # Elimina un usuario por su ID
        Usuario.objects.filter(id=usuario_id).delete()


# -------------------------------------
# MODELO DE HISTORIAL MÉDICO
# -------------------------------------
class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)  # Se registra automáticamente la fecha
