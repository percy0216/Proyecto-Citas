import { Especialidad } from './especialidad.models';
import { Paciente } from './paciente.models';
import { Medico } from './medico.models';

export interface Cita {
  id: number;
  fecha: string | Date;
  hora: string;
  estado: 'pendiente' | 'confirmada' | 'cancelada' | 'atendida';
  especialidad: Especialidad; 
  paciente: Paciente;         
  medico: Medico;             
}