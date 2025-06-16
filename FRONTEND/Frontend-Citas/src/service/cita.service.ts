// Importamos HttpClient para hacer peticiones HTTP
import { HttpClient } from '@angular/common/http';

// Importamos Injectable para que el servicio se pueda inyectar en otras clases
import { Injectable } from '@angular/core';

// Importamos el modelo de Cita que vamos a usar
import { Cita } from '../models/cita.models';

// Importamos Observable para manejar las respuestas asíncronas de las peticiones HTTP
import { Observable } from 'rxjs';

// Decorador que indica que este servicio se puede inyectar en cualquier parte del proyecto
@Injectable({
  providedIn: 'root' // hace que este servicio esté disponible en toda la aplicación
})
export class CitaService {

  // URL base de la API donde se registran las citas
  private apiUrl = 'http://127.0.0.1:8000/api/citas/';

  // Inyectamos el cliente HTTP para poder hacer peticiones
  constructor(private http: HttpClient) {}

  // Método para registrar una nueva cita
  registrarCita(cita: Cita): Observable<Cita> {
    // Enviamos la cita al backend mediante una petición POST
    return this.http.post<Cita>(this.apiUrl, cita);
  }
}
