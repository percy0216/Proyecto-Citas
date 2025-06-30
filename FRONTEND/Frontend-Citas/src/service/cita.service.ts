import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class CitaService {
  citaForm: FormGroup;
  especialidades: any[] = [];
  medicos: any[] = [];

  constructor(private route: Router, private apiservice: ApiService, private http: HttpClient ) { }

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
      console.log('Médicos:', this.medicos);
    });
  }

  registrarCita(citaData: any): Observable<any> {
    // Si el formulario es válido, puedes enviar los datos al servidor
    // if (this.citaForm.valid) {
    // console.log(this.citaForm.value); 
    return this.http.post<any>('http://127.0.0.1:8000/api/reservarcita/', citaData);
  }
}
