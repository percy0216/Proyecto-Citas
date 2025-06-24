import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { OnInit } from '@angular/core';
import { CitaService } from '../service/cita.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';

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

  constructor(private citaService: CitaService) { }

  ngOnInit(): void {
    this.citaForm = new FormGroup({
      fecha: new FormControl('', Validators.required),
      hora: new FormControl('', Validators.required),
      especialidad: new FormControl('', Validators.required),
      medico: new FormControl('', Validators.required),
      paciente: new FormControl('', Validators.required)
    });

    // Obtener especialidades
    this.citaService.getEspecialidades().subscribe(
      (data) => {
        this.especialidades = data;
      },
      // Especificamos el tipo del parámetro 'error'
      (error: HttpErrorResponse) => {
        console.error('Error al obtener las especialidades', error);
      }
    );

    // Obtener médicos
    this.citaService.getMedicos().subscribe(
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
      console.log('Cita reservada con los siguientes datos:', citaData);

      // Aquí puedes manejar el envío de datos al backend
      this.citaService.registrarCita(citaData).subscribe(
        (response) => {
          console.log('Cita registrada con éxito:', response);
        },
        // Especificamos el tipo del parámetro 'error'
        (error: HttpErrorResponse) => {
          console.error('Error al registrar la cita', error);
        }
      );
    }
  }
}