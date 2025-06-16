from rest_framework import routers
from . import views
from django.urls import path, include



# Se crea un enrutador por defecto para registrar los viewsets
router = routers.DefaultRouter()


# Aqui registra las rutas para cada recurso del sistema, usando los viewsets definidos en views.py

router.register('usuario', views.UsuarioViewsets)  # CRUD para usuarios
router.register('paciente', views.PacienteViewsets)  # CRUD para pacientes
router.register('especialidad', views.EspecialidadViewsets)  # CRUD para especialidades médicas
router.register('medico', views.MedicoViewsets)  # CRUD para médicos
router.register('cita', views.CitaViewsets)  # CRUD para citas médicas
router.register('registrovisitas', views.RegistroVisitasViewsets)  # CRUD para registros de visitas
router.register('administrador', views.AdministradorViewsets)  # CRUD para administradores
router.register('historialmedico', views.HistorialMedicoViewsets)  # CRUD para historiales médicos


# Define las rutas personalizadas y las del router

urlpatterns = [
    path('', include(router.urls)),                                     # Incluye automáticamente todas las rutas de los viewsets
    path('login/', views.LoginView.as_view(), name='login/'),           # Ruta para inicio de sesión
    path('registro/', views.RegistroView.as_view(), name='registro/'),  # Ruta para registro de nuevos usuarios
    
]
