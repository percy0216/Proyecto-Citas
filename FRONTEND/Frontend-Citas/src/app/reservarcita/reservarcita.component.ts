import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CitaService } from '../../service/cita.service';
import { Cita } from '../../models/cita.models';

@Component({
  selector: 'app-reservarcita',
  standalone: false,
  templateUrl: './reservarcita.component.html',
  styleUrl: './reservarcita.component.css'
})
export class ReservarcitaComponent {
 citaForm!: FormGroup;

  constructor(private fb: FormBuilder, private citaService: CitaService) {}

  ngOnInit(): void {
    this.citaForm = this.fb.group({
      fecha: ['', Validators.required],
      hora: ['', Validators.required],
      especialidad: ['', Validators.required],
      medico: ['', Validators.required],
      paciente: ['', Validators.required]
    });
  }

  registrar(): void {
    if (this.citaForm.valid) {
      const cita: Cita = this.citaForm.value;
      this.citaService.registrarCita(cita).subscribe({
        next: res => {
          console.log('Cita registrada:', res);
          alert('Cita registrada correctamente');
        },
        error: err => {
          console.error('Error al registrar cita:', err);
          alert('Error al registrar la cita');
        }
      });
    }
  }
}
