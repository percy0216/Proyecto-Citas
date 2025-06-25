import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  username = '';
  password = '';
  error = '';

  constructor(private auth: AuthService, private router: Router) {}



  // onCaptchaResolved(token: string | null) {
  //   if (token) {
  //   console.log('reCAPTCHA resuelto:', token);
  //   // Aquí puedes guardar el token o validarlo con el backend si lo necesitas
  // } else {
  //   console.warn('reCAPTCHA no completado');
  // }
  // }


  login() {
  this.auth.login(this.username, this.password).subscribe({
    next: (res: any) => {
      console.log('Respuesta del backend:', res);
      localStorage.setItem('token', res.token);
      localStorage.setItem('usuario', JSON.stringify(res.usuario));

      const tipo = res.usuario.tipo_usuario;

      if (tipo === 'admin') {
        this.router.navigate(['/panel-admin-9472']);
      } else if (tipo === 'medico') {
        this.router.navigate(['/medico']);
      } else {
        this.router.navigate(['/home']);
      }
    },

    error: () => {
      this.error = 'Usuario y/o contraseña incorrectos';
    }
    
    });
  }



}
