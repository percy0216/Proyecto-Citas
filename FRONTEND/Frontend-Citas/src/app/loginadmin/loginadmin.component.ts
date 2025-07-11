import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';
import { Usuario } from '../../models/usuario.models';
import { ApiService } from '../../service/api.service';
import { Especialidad } from '../../models/especialidad.models';

@Component({
  selector: 'app-loginadmin',
  standalone: false,
  templateUrl: './loginadmin.component.html',
  styleUrl: './loginadmin.component.css'
})
export class LoginadminComponent implements OnInit {
  mostrarmodal: boolean = false;
  usuarioseleccionado: Usuario | null = null;
  editando: boolean = false;
  usuarios: any[] = [];
  esAdmin: boolean = false;

  // ===== MÉDICO =====
  mostrarModalMedico: boolean = false;
  especialidades: Especialidad[] = [];
  nuevoMedico: any = {
    usuario: {
      nombre: '',
      apellido: '',
      username: '',
      password: '',
      dni: '',
      email: '',
      telefono: '',
      tipo_usuario: 'medico'
    },
    especialidad: null,
    horario_libre: ''
  };

  // ===== ESPECIALIDAD =====
  mostrarFormularioEspecialidad: boolean = false;
  nuevaEspecialidad: Especialidad = {
    id: 0,
    nombre: '',
    descripcion: ''
  };

  constructor(
    private http: HttpClient,
    private auth: AuthService,
    private router: Router,
    private apiservice: ApiService
  ) {}

  ngOnInit(): void {
    const tipo = this.auth.getTipoUsuario();

    if (tipo === 'admin') {
      this.esAdmin = true;
      this.cargarUsuarios();
      this.apiservice.getEspecialidades().subscribe({
        next: data => this.especialidades = data,
        error: err => console.error('Error al cargar especialidades:', err)
      });
    } else {
      alert('No tienes permisos para acceder a esta página');
      this.router.navigate(['/login']);
    }
  }

  cargarUsuarios(): void {
    this.http.get<any[]>('http://127.0.0.1:8000/api/usuario/').subscribe({
      next: data => this.usuarios = data,
      error: err => console.error('Error al cargar usuarios:', err)
    });
  }

  verUsuario(usuario: any): void {
    this.usuarioseleccionado = usuario;
    this.mostrarmodal = true;
  }

  cerrarModal(): void {
    this.mostrarmodal = false;
    this.usuarioseleccionado = null;
  }

  habilitarEdicion() {
    this.editando = true;
  }

  cancelarEdicion() {
    this.editando = false;
  }

  guardarCambios() {
    if (this.usuarioseleccionado) {
      this.apiservice.putUsuario(this.usuarioseleccionado).subscribe({
        next: () => {
          this.editando = false;
          alert('Usuario actualizado correctamente');
        },
        error: () => {
          alert('Error al actualizar usuario');
        }
      });
    }
  }

  eliminarUsuario(id: number): void {
    if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
      this.http.delete(`http://127.0.0.1:8000/api/usuario/${id}/`).subscribe({
        next: () => {
          this.cargarUsuarios();
        },
        error: err => console.error('Error al eliminar:', err)
      });
    }
  }

  cerrarSesion() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }

  // ========== MÉDICO ==========
  abrirModalMedico() {
    this.mostrarModalMedico = true;
  }

  cerrarModalMedico() {
    this.mostrarModalMedico = false;
    this.resetFormularioMedico();
  }

  resetFormularioMedico() {
    this.nuevoMedico = {
      usuario: {
        nombre: '',
        apellido: '',
        username: '',
        password: '',
        dni: '',
        email: '',
        telefono: '',
        tipo_usuario: 'medico'
      },
      especialidad: null,
      horario_libre: ''
    };
  }

  registrarMedico() {
    if (!this.nuevoMedico.usuario.username || !this.nuevoMedico.usuario.password || !this.nuevoMedico.especialidad) {
      alert('Completa los campos obligatorios');
      return;
    }

    this.apiservice.postMedico(this.nuevoMedico).subscribe({
      next: () => {
        alert('Médico registrado correctamente');
        this.cerrarModalMedico();
        this.cargarUsuarios();
      },
      error: () => {
        alert('Error al registrar médico');
      }
    });
  }

  // ========== ESPECIALIDAD ==========
  registrarEspecialidad() {
    if (!this.nuevaEspecialidad.nombre || !this.nuevaEspecialidad.descripcion) {
      alert('Por favor, completa todos los campos');
      return;
    }

    this.apiservice.postEspecialidad(this.nuevaEspecialidad).subscribe({
      next: () => {
        alert('Especialidad registrada correctamente');
        this.mostrarFormularioEspecialidad = false;
        this.nuevaEspecialidad = { id: 0, nombre: '', descripcion: '' };
        this.apiservice.getEspecialidades().subscribe(data => this.especialidades = data); // refresca lista
      },
      error: () => {
        alert('Error al registrar especialidad');
      }
    });
  }

  cancelarEspecialidad() {
    this.mostrarFormularioEspecialidad = false;
    this.nuevaEspecialidad = { id: 0, nombre: '', descripcion: '' };
  }
}
