import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { OnInit } from '@angular/core';
import { CitaService } from '../../service/cita.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { ApiService } from '../../service/api.service';

@Component({
  selector: 'app-reservar-cita',
  standalone: false,
  templateUrl: './reservar-cita.component.html',
  styleUrl: './reservar-cita.component.css'
})

export class ReservarCitaComponent implements OnInit {
  citaForm: FormGroup;
  especialidades: any[] = [];
  medicos: any[] = [];

  constructor(private apiService: ApiService , private citaService:CitaService , private fb : FormBuilder) { }

   ngOnInit(): void {
    // Inicializa el formulario con validaciones
    this.citaForm = this.fb.group({
      especialidad: ['', Validators.required],
      medico: ['', Validators.required],
      fecha: ['', Validators.required]
    });

    // Obtener especialidades
    this.apiService.getEspecialidades().subscribe(
      (data) => {
        this.especialidades = data;
      },
      // Especificamos el tipo del parámetro 'error'
      (error: HttpErrorResponse) => {
        console.error('Error al obtener las especialidades', error);
      }
    );

    // Obtener médicos
    this.apiService.getMedicos().subscribe(
      (data) => {
        this.medicos = data;
      },
      // Especificamos el tipo del parámetro 'error'
      (error: HttpErrorResponse) => {
        console.error('Error al obtener los médicos', error);
      }
    );
  }

registrar(): void {
  if (this.citaForm.valid) {
    const citaData = this.citaForm.value;
    console.log('Datos enviados:', citaData);  // Verifica los datos

    this.citaService.registrarCita(citaData).subscribe(
      (response) => {
        console.log('Cita registrada con éxito:', response);
      },
      (error) => {
        console.error('Error al registrar la cita', error);
      }
    );
  }
}

}