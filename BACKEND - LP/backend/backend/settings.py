from pathlib import Path  # Importamos la clase Path para manejar rutas del sistema de archivos

# Establece la ruta base del proyecto (la carpeta principal del proyecto)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta que Django usa para seguridad (¡nunca se comparte en producción!)
SECRET_KEY = 'django-insecure-os%ek$=l$cf!8$pnn#fwuj9^#hf0b=iavp6-dvc*77x2s1m%3h'

# Si está en True, muestra errores detallados en el navegador (solo para desarrollo)
DEBUG = True

# Lista de dominios que pueden acceder a la app (vacía en desarrollo)
ALLOWED_HOSTS = []

# Aquí le decimos a Django que usaremos un modelo de usuario personalizado llamado "Usuario"
# que está dentro de la app "api"
AUTH_USER_MODEL = 'api.Usuario'

# Lista de aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'api',                      # Nuestra app personalizada
    'rest_framework',           # Framework para crear APIs
    'rest_framework.authtoken', # Permite usar autenticación por token
    'corsheaders',              # Permite que el frontend pueda conectarse al backend (CORS)
    'django.contrib.admin',     # Interfaz de administración de Django
    'django.contrib.auth',      # Sistema de autenticación
    'django.contrib.contenttypes',  # Tipos de contenido (sirve para relacionar modelos)
    'django.contrib.sessions',  # Manejo de sesiones (login, cookies, etc.)
    'django.contrib.messages',  # Sistema de mensajes (notificaciones)
    'django.contrib.staticfiles',  # Manejo de archivos estáticos (CSS, JS, imágenes)
]

# Configuración del framework REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Autenticación por token
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Requiere que el usuario esté autenticado
    ],
}

# Middleware: procesos que se ejecutan antes o después de cada petición/respuesta
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Habilita CORS (conexión con frontend)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'api.middleware.ApiKeyMiddleware',  # Middleware propio para verificar API KEY (si se usa)
]

# Clave para autenticar peticiones a través de una API Key (usado si creas tu propio middleware)
API_KEY = 'iEpeJsgQbWzbNEirdKEWnYPf'

# Dominios o direcciones permitidas desde donde el frontend puede hacer peticiones al backend
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',  # Dirección local del backend
    'http://localhost:4200',  # Dirección local del frontend (Angular)
]

# Cabeceras permitidas en las peticiones CORS
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-api-key',  # Permite el uso de una API KEY personalizada
]

# Métodos HTTP permitidos en las peticiones CORS
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Archivo que contiene la configuración de las rutas del proyecto
ROOT_URLCONF = 'backend.urls'

# Configuración para las plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directorios donde buscar plantillas HTML personalizadas
        'APP_DIRS': True,  # Buscar plantillas dentro de las apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Archivo que lanza la aplicación en producción con WSGI (servidor compatible con Python)
WSGI_APPLICATION = 'backend.wsgi.application'

# Configuración de la base de datos (usamos SQLite por defecto, ideal para desarrollo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos
        'NAME': BASE_DIR / 'db.sqlite3',  # Nombre del archivo de la base de datos
    }
}

# Validaciones para contraseñas de usuarios
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # No usar datos personales
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Longitud mínima
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Evita contraseñas comunes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Evita solo números
    },
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'en-us'  # Idioma por defecto
TIME_ZONE = 'UTC'  # Zona horaria

USE_I18N = True  # Soporte para múltiples idiomas
USE_TZ = True  # Usa zonas horarias reales

# URL para archivos estáticos (como CSS, JS, imágenes)
STATIC_URL = 'static/'

# Tipo de campo para claves primarias automáticas por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
