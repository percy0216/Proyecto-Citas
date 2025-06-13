import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-registro',
  standalone: false,
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css',
})
export class RegistroComponent implements OnInit {
  registroForm!: FormGroup;

  constructor(private fb: FormBuilder, private auth: AuthService) {}

  ngOnInit(): void {
    this.registroForm = this.fb.group({
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      dni: ['', Validators.required],
      correo: ['', [Validators.required, Validators.email]],
      telefono: [''],
      username: ['', Validators.required], 
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  registrar(): void {
  if (this.registroForm.valid) {
    const datos = this.registroForm.value;
    datos.tipo_usuario = 'paciente';

    console.log('Datos enviados:', datos);
    this.auth.registrar(datos).subscribe({
      next: (res) => {
        console.log('Usuario registrado:', res);
        alert('Usuario registrado correctamente');
      },
      error: (err) => {
        console.error('Error al registrar:', err);
        alert('Error al registrar usuario');
      }
    });
  }
}
}


