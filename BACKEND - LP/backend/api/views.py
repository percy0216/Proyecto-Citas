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
from .serializers import CitaSerializers
from .serializers import PacienteRegistroSerializer
import requests
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ReservarCitaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CitaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Cita reservada correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # captcha = request.data.get("captcha")
        # if not captcha:
        #     return Response({"error": "Captcha requerido"}, status=400)

        # # Verificar con Google
        # captcha_verificado = requests.post("https://www.google.com/recaptcha/api/siteverify", data={
        #     'secret': '6LfCkWYrAAAAAJ43W1Wca68I8JSYEBVJQj-QNzY0',
        #     'response': captcha
        # }).json()

        # if not captcha_verificado.get("success"):
        #     return Response({"error": "Captcha inválido"}, status=400)

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
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
                'tipo_usuario': user.tipo_usuario
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




class UsuarioViewsets(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return serializers.PerfilUsuarioSerializer
        return serializers.UsuarioSerializers


class PacienteViewsets (viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializers

class PacienteIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            paciente = models.Paciente.objects.get(usuario=request.user)
            return Response({'paciente_id': paciente.id}, status=status.HTTP_200_OK)
        except models.Paciente.DoesNotExist:
            return Response({'error': 'No es un paciente'}, status=status.HTTP_404_NOT_FOUND)


class EspecialidadViewsets (viewsets.ModelViewSet):
    queryset = models.Especialidad.objects.all()
    serializer_class = serializers.EspecialidadSerializers


class MedicoViewsets(viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['especialidad']
        

class HorarioViewsets (viewsets.ModelViewSet):
    queryset = models.Horario.objects.all()
    serializer_class = serializers.HorarioSerializers

# class CitaViewsets (viewsets.ModelViewSet):
#     queryset = models.Cita.objects.all()
#     serializer_class = serializers.CitaSerializers

class CitaViewsets(viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.CitaReadSerializers
        return CitaSerializers


class RegistroVisitasViewsets (viewsets.ModelViewSet):
    queryset = models.RegistroVisitas.objects.all()
    serializer_class = serializers.RegistroVisitasSerializers


class AdministradorViewsets (viewsets.ModelViewSet):
    queryset = models.Administrador.objects.all()
    serializer_class = serializers.AdministradorSerializers


class HistorialMedicoViewsets (viewsets.ModelViewSet):
    queryset = models.HistorialMedico.objects.all()
    serializer_class = serializers.HistorialMedicoSerializers
