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
  pacientes: any[] = []; // Lista de pacientes, si es necesario

  constructor(private apiService: ApiService, private citaService: CitaService, private fb: FormBuilder) { }

  ngOnInit(): void {
    this.citaForm = this.fb.group({
      especialidad: ['', Validators.required],
      medico: ['', Validators.required],
      fecha: ['', Validators.required],
      horaAtencion: ['', Validators.required],
      paciente: ['', Validators.required],  
    });

    this.apiService.getEspecialidades().subscribe(
      (data) => {
        this.especialidades = data;
      },
      (error: HttpErrorResponse) => {
        console.error('Error al obtener las especialidades', error);
      }
    );

    this.apiService.getMedicos().subscribe(
      (data) => {
        this.medicos = data;
      },
      (error: HttpErrorResponse) => {
        console.error('Error al obtener los médicos', error);
      }
    );

    // Si necesitas obtener pacientes para llenar el select
    this.apiService.getPacientes().subscribe(
      (data) => {
        this.pacientes = data;
        console.log('Pacientes:', this.pacientes);
      },
      (error: HttpErrorResponse) => {
        console.error('Error al obtener los pacientes', error);
      }
    );
  }

 registrar(): void {
  if (this.citaForm.valid) {
    console.log('pacienteseleccionado en el formulario:', this.citaForm.value.paciente);

    const citaData = this.citaForm.value;

    const adjustedData = {
      especialidad: citaData.especialidad,
      medico: citaData.medico,
      fecha: citaData.fecha,
      hora: citaData.horaAtencion, 
      paciente: citaData.paciente || null,  
    };

    console.log('Datos enviados al backend:', adjustedData);

    this.citaService.registrarCita(adjustedData).subscribe(
      (response) => {
        console.log('Cita registrada con éxito:', response);
      },
      (error: HttpErrorResponse) => {
        console.error('Detalles del error:', error);
        if (error.error) {
          console.error('Mensaje del backend:', error.error);  // Aquí verás el mensaje del servidor
        }
      }
    );
  } else {
    console.error('Formulario no válido');
  }
}
  
}
