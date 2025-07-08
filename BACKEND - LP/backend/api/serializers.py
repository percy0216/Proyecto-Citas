from rest_framework import serializers 
from . import models

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    direccion = serializers.CharField(source='paciente.direccion', allow_blank=True, required=False)

    class Meta:
        model = models.Usuario
        fields = ['first_name', 'last_name', 'email', 'dni', 'telefono', 'direccion']

    def update(self, instance, validated_data):
        paciente_data = validated_data.pop('paciente', {})
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()

        if hasattr(instance, 'paciente') and paciente_data:
            instance.paciente.direccion = paciente_data.get('direccion', instance.paciente.direccion)
            instance.paciente.save()

        return instance


class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class PacienteRegistroSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializers()  

    class Meta:
        model = models.Paciente
        fields = ['usuario','fecha_nacimiento', 'direccion']  

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['tipo_usuario'] = 'paciente'
        user = models.Usuario.objects.create_user(**usuario_data)
        paciente = models.Paciente.objects.create(usuario=user, **validated_data)
        return paciente

class EspecialidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidad
        fields = '__all__'

class MedicoSerializers(serializers.ModelSerializer):
    usuario = UsuarioSerializers()
    especialidad = EspecialidadSerializers()

    class Meta:
        model = models.Medico
        fields = ["id", "usuario", "horario_libre", "especialidad"]

class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'

class CitaReadSerializers(serializers.ModelSerializer):
    especialidad = EspecialidadSerializers()
    medico = MedicoSerializers()
    class Meta:
        model = models.Cita
        fields = '__all__'

class CitaSerializers(serializers.ModelSerializer):
    especialidad = serializers.PrimaryKeyRelatedField(queryset=models.Especialidad.objects.all())
    medico = serializers.PrimaryKeyRelatedField(queryset=models.Medico.objects.all())
    paciente = serializers.PrimaryKeyRelatedField(queryset=models.Paciente.objects.all())

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


