import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

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
        return this.http.post(this.loginUrl, { username, password });
    }

    isAuthenticated(): boolean {
        const token = localStorage.getItem('token');
        return !!token;
    }

    logout() {
        localStorage.removeItem('token');
    }
}
