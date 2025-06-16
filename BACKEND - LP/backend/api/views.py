from django.shortcuts import render
from . import models, serializers                       # Importa los models y serializadores 
from rest_framework import viewsets                     # Para crear vistas basadas en ViewSets
from rest_framework.response import Response            # Para enviar respuestas personalizadas
from rest_framework.authtoken.models import Token       # Para generar y validar tokens de autenticación
from rest_framework.views import APIView                # Para crear vistas API personalizadas
from rest_framework.permissions import AllowAny         # Permite acceso sin autenticación
from django.contrib.auth import authenticate            # Autenticación de usuarios
from rest_framework import status                       # Códigos HTTP estándar
from django.contrib.auth import get_user_model          # Para usar el modelo de usuario personalizado
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt    
from rest_framework.permissions import IsAuthenticated  # Requiere autenticación


# ------------------------------------------------
# Vista personalizada para reservar una cita
# ------------------------------------------------

class ReservarCitaView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden reservar

    def post(self, request):
        serializer = CitaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Cita reservada correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------
# Vista personalizada para login de usuario
# ------------------------------------------------



class LoginView(APIView):
    permission_classes = [AllowAny]  # No requiere autenticación para acceder al login

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)  # Verifica credenciales

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)  # Genera token si es válido
            return Response({"token": token.key})  # Devuelve token
        else:
            return Response({"error": "Credenciales Invalidas"}, status=400)



# ------------------------------------------------
# Vista para registrar usuarios nuevos
# ------------------------------------------------



User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')  # Exime protección CSRF
class RegistroView(APIView):
    permission_classes = [AllowAny]  # Cualquiera puede registrarse

    def post(self, request):
        data = request.data

        try:
            # Crea usuario con los campos básicos
            user = User.objects.create_user(
                username=data.get('username'),
                email=data.get('correo'),
                password=data.get('password')
            )

            # Asigna campos personalizados adicionales
            user.nombre = data.get('nombre')
            user.apellido = data.get('apellido')
            user.dni = data.get('dni')
            user.telefono = data.get('telefono')
            user.tipo_usuario = 'paciente'  # Siempre se crea como paciente

            user.save()

            return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ------------------------------------------------
# VISTAS BASADAS EN MODELOS PARA CRUD AUTOMÁTICO
# ---------------------------------------------------


# CRUD de Usuarios
class UsuarioViewsets(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializers

# CRUD de Pacientes
class PacienteViewsets(viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializers

# CRUD de Especialidades médicas
class EspecialidadViewsets(viewsets.ModelViewSet):
    queryset = models.Especialidad.objects.all()
    serializer_class = serializers.EspecialidadSerializers

# CRUD de Médicos
class MedicoViewsets(viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializers

# CRUD de Citas médicas
class CitaViewsets(viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.CitaSerializers

# CRUD de registros de visitas
class RegistroVisitasViewsets(viewsets.ModelViewSet):
    queryset = models.RegistroVisitas.objects.all()
    serializer_class = serializers.RegistroVisitasSerializers

# CRUD de Administradores
class AdministradorViewsets(viewsets.ModelViewSet):
    queryset = models.Administrador.objects.all()
    serializer_class = serializers.AdministradorSerializers

# CRUD del Historial Médico
class HistorialMedicoViewsets(viewsets.ModelViewSet):
    queryset = models.HistorialMedico.objects.all()
    serializer_class = serializers.HistorialMedicoSerializers
