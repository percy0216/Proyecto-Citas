from django.shortcuts import render
from . import models,serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializers import citaSerializers
from .serializers import PacienteRegistroSerializer
from .serializers import ReservarCitaSerializers

class ReservarCitaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReservarCitaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Cita reservada correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            # ✅ NUEVO BLOQUE: obtener paciente_id si es paciente
            paciente_id = None
            if user.tipo_usuario == 'paciente':
                try:
                    paciente_id = user.paciente.id
                except:
                    pass  # O puedes lanzar un error aquí si lo prefieres

            return Response({
                "token": token.key,
                'usuario': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.nombre,
                    'last_name': user.apellido,
                    'email': user.email,
                    'dni': user.dni,
                    'telefono': user.telefono,
                    'tipo_usuario': user.tipo_usuario,
                    'paciente_id': paciente_id
                }
            })
        else:
            return Response({"error": "Credenciales Invalidas"}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class RegistroPacienteView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PacienteRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Paciente registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UsuarioViewsets (viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializers


class PacienteViewsets (viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializers


class EspecialidadViewsets (viewsets.ModelViewSet):
    queryset = models.Especialidad.objects.all()
    serializer_class = serializers.EspecialidadSerializers


class MedicoViewsets (viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializers


class CitaViewsets (viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.citaSerializers


class RegistroVisitasViewsets (viewsets.ModelViewSet):
    queryset = models.RegistroVisitas.objects.all()
    serializer_class = serializers.RegistroVisitasSerializers


class AdministradorViewsets (viewsets.ModelViewSet):
    queryset = models.Administrador.objects.all()
    serializer_class = serializers.AdministradorSerializers


class HistorialMedicoViewsets (viewsets.ModelViewSet):
    queryset = models.HistorialMedico.objects.all()
    serializer_class = serializers.HistorialMedicoSerializers
