#------------------------------------------------------------------------------
# -----------------------¿Qué hace este middleware?-----------------------------
#-------------------------------------------------------------------------------
# Protege rutas verificando que cada petición incluya una clave (x-api-key) válida.
# Exceptúa la ruta /api/registro/ para que se pueda acceder sin clave (útil para registrar usuarios).
# Si no hay clave o es incorrecta, devuelve un error 403 con un mensaje.



from django.conf import settings  # Importa la configuración global del proyecto (para usar la API_KEY)
from django.http import JsonResponse  # Permite devolver respuestas JSON (como error 403)

# Esta clase es un middleware personalizado para verificar si la petición tiene una API Key válida
class ApiKeyMiddleware:
    # Este método se ejecuta al inicializar el middleware
    def __init__(self, get_response):
        self.get_response = get_response  # Guarda la función que manejará la respuesta

    # Este método se ejecuta cada vez que llega una petición HTTP al servidor
    def __call__(self, request):
        # Permitir que las peticiones a /api/registro/ pasen sin validar la API Key
        if request.path == '/api/registro/':
            return self.get_response(request)

        # Obtiene la API Key desde los encabezados de la petición (header: x-api-key)
        api_key = request.headers.get('x-api-key')

        # Compara la clave enviada con la clave definida en settings.py
        if api_key != settings.API_KEY:
            # Si no coinciden, se devuelve un error 403 (Prohibido)
            return JsonResponse({'error': 'Invalid API Key'}, status=403)

        # Si la API Key es válida, se continúa con la petición
        return self.get_response(request)
