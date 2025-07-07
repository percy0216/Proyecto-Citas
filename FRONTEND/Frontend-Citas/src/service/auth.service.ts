import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { tap } from "rxjs";

@Injectable({
    providedIn: 'root'
})

export class AuthService {
    private loginUrl = 'http://127.0.0.1:8000/api/login/';
    private registroUrl = 'http://127.0.0.1:8000/api/registro/'; 
    apiKey= 'iEpeJsgQbWzbNEirdKEWnYPf';

    constructor(private http: HttpClient) {}

    registrar(datos: any) {
        const headers = new HttpHeaders({
        'Content-Type': 'application/json',
        'x-api-key': this.apiKey
        });

        return this.http.post(this.registroUrl, datos, { headers });
    }

    login(username: string, password: string) {
        return this.http.post<any>(this.loginUrl, { username, password }).pipe(
            // Requiere que instales RxJS si aún no lo tienes
            // npm install rxjs
            // o asegúrate de tener importado `map`, `tap` o similar
            tap((response) => {
            localStorage.setItem('token', response.token);

            // ✅ Guardamos paciente_id si existe
            if (response.usuario && response.usuario.paciente_id) {
                localStorage.setItem('paciente_id', response.usuario.paciente_id.toString());
            }
            })
        );
        }
        
        isAuthenticated(): boolean {
        const token = localStorage.getItem('token');
        return !!token;
    }

    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('paciente_id');
    }

    getPacienteId(): number | null {
        const id = localStorage.getItem('paciente_id');
        return id ? parseInt(id, 10) : null;
    }
    }
