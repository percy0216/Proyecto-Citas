// Importamos los decoradores e interfaces necesarias
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router'; // CanActivate permite proteger rutas
import { AuthService } from './auth.service'; // Servicio que maneja la autenticación

@Injectable({
  providedIn: 'root' // Hace que el guard esté disponible globalmente en la app
})
export class AuthGuard implements CanActivate {
  // Inyectamos el AuthService para verificar si el usuario está autenticado
  // Inyectamos el Router para redirigir si no está autenticado
  constructor(private auth: AuthService, private router: Router) {}

  // Método obligatorio de la interfaz CanActivate
  // Devuelve true si el usuario puede acceder a la ruta, false si no
  canActivate(): boolean {
    // Verificamos si el usuario está autenticado usando AuthService
    if (this.auth.isAuthenticated()) {
      return true; // Permite el acceso a la ruta protegida
    } else {
      this.router.navigate(['/login']); // Redirige al login si no está autenticado
      return false; // Bloquea el acceso a la ruta
    }
  }
}
