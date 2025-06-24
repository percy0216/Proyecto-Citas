import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Cita } from '../models/cita.models';
import { Observable } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Especialidad } from '../models/especialidad.models';
import { Medico } from '../models/medico.models';
import { Router } from '@angular/router';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class CitaService {
  citaForm: FormGroup;
  especialidades: any[] = [];
  medicos: any[] = [];

  constructor(private citaService: CitaService, private route: Router, private apiservice: ApiService) { }

  ngOnInit() {
    this.citaForm = new FormGroup({
      fecha: new FormControl('', Validators.required),
      hora: new FormControl('', Validators.required),
      especialidad: new FormControl('', Validators.required),
      medico: new FormControl('', Validators.required),
      paciente: new FormControl('', Validators.required)
    });

    // Obtener especialidades
    this.apiservice.getEspecialidades().subscribe(data => {
      this.especialidades = data;
    });

    // Obtener médicos
    this.apiservice.getMedicos().subscribe(data => {
      this.medicos = data;
    });
  }

  registrar() {
    if (this.citaForm.valid) {
      console.log(this.citaForm.value); // Enviar los datos al servidor
    }
  }
}