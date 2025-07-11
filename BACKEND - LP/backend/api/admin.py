from django.contrib import admin
from .models import Usuario, Paciente, Especialidad, Medico, Horario, Cita, RegistroVisitas, Administrador, HistorialMedico

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Horario)
admin.site.register(Cita)
admin.site.register(RegistroVisitas)
admin.site.register(Administrador)
admin.site.register(HistorialMedico)
