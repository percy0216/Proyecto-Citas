// ----------- ¿Qué hace el interceptor? ---------------

// Este interceptor:
// Intercepta todas las peticiones HTTP hechas desde Angular.
// Verifica si hay un token guardado en el localStorage.
// Si la URL no es de login, añade el Authorization con el token y una X-API-KEY estándar.
// Si la URL es de login, solo añade una X-API-KEY específica para autenticación.
// Pasa la petición (modificada o no) al siguiente interceptor o directamente al servidor.




// Importamos Injectable para poder usar el interceptor como servicio inyectable
import { Injectable } from '@angular/core';

// Importamos las clases necesarias para interceptar peticiones HTTP
import { HttpInterceptor, HttpRequest, HttpHandler } from '@angular/common/http';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  
  // Método que se ejecuta automáticamente en cada petición HTTP
  intercept(req: HttpRequest<any>, next: HttpHandler) {

    // Obtenemos el token almacenado en localStorage
    const token = localStorage.getItem('token');

    // Si hay token y la URL NO es para login, añadimos el token al encabezado Authorization
    if (token && !req.url.includes('/api/login/')) {
      req = req.clone({
        setHeaders: {
          Authorization: `Token ${token}`, // Se añade el token de autenticación
          'X-API-KEY' : 'b91TXGCJEQmN8P7hrSP0urgl' // API Key para rutas normales (no login)
        }
      });
    }

    // Si la petición es para el login, se añade una API Key diferente
    if (req.url.includes('/api/login/')) {
      req = req.clone({
        setHeaders: {
          'X-API-KEY' : 'iEpeJsgQbWzbNEirdKEWnYPf' // API Key especial solo para login
        }
      });
    }

    // Continuamos con la ejecución de la petición modificada (o no modificada)
    return next.handle(req);
  }
}
