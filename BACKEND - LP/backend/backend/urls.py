from django.contrib import admin
from django.urls import path, include
from rest_framework import routers          # Importa los routers
from api import views                      
urlpatterns = [
    path('admin/', admin.site.urls),    # Ruta para acceder al panel de administración de Django
    path('api/', include('api.urls')),  # Incluye todas las rutas definidas en la app 'api'
]
