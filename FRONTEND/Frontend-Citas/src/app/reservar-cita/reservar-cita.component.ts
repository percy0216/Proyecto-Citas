import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-reservar-cita',
  standalone: false,
  templateUrl: './reservar-cita.component.html',
  styleUrl: './reservar-cita.component.css'
})

export class reservarcitacomponent implements OnInit {
  citaForm: FormGroup;

  ngOnInit() {
    this.citaForm = new FormGroup({
      fecha: new FormControl('', Validators.required),
      hora: new FormControl('', Validators.required),
      especialidad: new FormControl('', [Validators.required, Validators.min(1)]),
      medico: new FormControl('', [Validators.required, Validators.min(1)]),
      paciente: new FormControl('', [Validators.required, Validators.min(1)])
    });
  }

  registrar() {
    if (this.citaForm.valid) {
      console.log(this.citaForm.value); // Aquí puedes manejar el envío de datos a tu backend
    } else {
      console.log('Formulario inválido');
    }
  }
}