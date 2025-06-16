// Importamos los decoradores e interfaces necesarias
import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Injectable({
    providedIn: 'root' // Hace que el servicio esté disponible globalmente en la app
})
export class AuthService {
    // URL del backend para login y registro
    private loginUrl = 'http://127.0.0.1:8000/api/login/';
    private registroUrl = 'http://127.0.0.1:8000/api/registro/';

    // Clave API personalizada para el registro (opcional, depende de tu backend)
    apiKey = 'iEpeJsgQbWzbNEirdKEWnYPf';

    // Inyección de HttpClient para realizar peticiones HTTP
    constructor(private http: HttpClient) {}

    // Método para registrar un nuevo usuario
    registrar(datos: any) {
        // Se definen los headers con tipo JSON y una clave API
        const headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'x-api-key': this.apiKey
        });

        // Se hace una petición POST al endpoint de registro
        return this.http.post(this.registroUrl, datos, { headers });
    }

    // Método para hacer login (autenticación)
    login(username: string, password: string) {
        // Envia el usuario y la contraseña como un objeto JSON
        return this.http.post(this.loginUrl, { username, password });
    }

    // Verifica si el usuario está autenticado comprobando si hay un token en localStorage
    isAuthenticated(): boolean {
        const token = localStorage.getItem('token');
        return !!token; // Retorna true si hay token, false si no
    }

    // Método para cerrar sesión (elimina el token del localStorage)
    logout() {
        localStorage.removeItem('token');
    }
}
