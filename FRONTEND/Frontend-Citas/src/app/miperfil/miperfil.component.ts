import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-miperfil',
  standalone: false,
  templateUrl: './miperfil.component.html',
  styleUrl: './miperfil.component.css'
})
export class MiperfilComponent {
  perfilForm!: FormGroup;

  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router) {}

  ngOnInit(): void {
    const userData = localStorage.getItem('usuario');
    const usuario = userData ? JSON.parse(userData) : {};

    this.perfilForm = this.fb.group({
      first_name: [usuario.first_name || ''],
      last_name: [usuario.last_name || ''],
      email: [usuario.email || ''],
      dni: [usuario.dni || ''],
      telefono: [usuario.telefono || '']
    });
  }

  cerrarSesion() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }
}
