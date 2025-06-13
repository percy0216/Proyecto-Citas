from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register('Usuario', views.UsuarioViewsets)
# router.register('Paciente', views.PacienteViewsets)
# router.register('Especialidad', views.EspecialidadViewsets)
# router.register('Medico', views.MedicoViewsets)
# router.register('Cita', views.CitaViewsets)
# router.register('Registro Visitas', views.RegistroVisitasViewsets)
# router.register('Administrador', views.AdministradorViewsets)
# router.register('Historial Medico', views.HistorialMedicoViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
