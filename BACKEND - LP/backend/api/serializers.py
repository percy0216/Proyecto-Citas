
#------------------------------------- ¿QUE HACE UN SERIALIZER?-----------------------------------------------
# Un serializador convierte datos del modelo en formatos que se pueden enviar por API (como JSON), y viceversa.
# También ayuda a validar la información que llega desde una petición del usuario antes de guardarla en la base de datos.



from rest_framework import serializers 
from . import models  # Importamos los modelos definidos en models.py

# -------------------------------------
# SERIALIZADOR PARA USUARIO
# -------------------------------------
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario  # Modelo al que pertenece
        fields = '__all__'  # Incluye todos los campos del modelo

# -------------------------------------
# SERIALIZADOR PARA PACIENTE
# -------------------------------------
class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA ESPECIALIDAD
# -------------------------------------
class EspecialidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidad
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA MÉDICO
# -------------------------------------
class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA CITA
# -------------------------------------
class CitaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cita
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA REGISTRO DE VISITAS
# -------------------------------------
class RegistroVisitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.RegistroVisitas
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA ADMINISTRADOR
# -------------------------------------
class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Administrador
        fields = '__all__'

# -------------------------------------
# SERIALIZADOR PARA HISTORIAL MÉDICO
# -------------------------------------
class HistorialMedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.HistorialMedico
        fields = '__all__'
