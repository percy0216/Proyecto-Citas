import { Usuario } from './usuario.models';
import { Especialidad } from './especialidad.models';

export interface Medico {
  id: number;
  usuario: Usuario | number;
  especialidad: Especialidad | number;
  horario_libre?: string ;
}