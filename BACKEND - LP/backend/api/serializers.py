from rest_framework import serializers 
from . import models

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class PacienteRegistroSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializers()  # anidamos el serializer de Usuario

    class Meta:
        model = models.Paciente
        fields = ['usuario','fecha_nacimiento', 'direccion']  # agrega tus campos propios de Paciente

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['tipo_usuario'] = 'paciente'  # aseguramos que siempre sea paciente
        user = models.Usuario.objects.create_user(**usuario_data)
        paciente = models.Paciente.objects.create(usuario=user, **validated_data)
        return paciente

class EspecialidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidad
        fields = '__all__'

class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'

class CitaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cita
        fields = '__all__'

class RegistroVisitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.RegistroVisitas
        fields = '__all__'

class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Administrador
        fields = '__all__'

class HistorialMedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.HistorialMedico
        fields = '__all__'


