import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';
import { Usuario } from '../../models/usuario.models';
import { ApiService } from '../../service/api.service';

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
  
  constructor(private http: HttpClient, private auth: AuthService, private router: Router,private apiservice: ApiService) {}

  ngOnInit(): void {

    const tipo = this.auth.getTipoUsuario();

    if (tipo === 'admin') {
      this.esAdmin = true;
      this.cargarUsuarios();
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
      console.log('Ver usuario:', usuario);
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
    this.apiservice.putUsuario( this.usuarioseleccionado).subscribe({
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
          console.log('Usuario eliminado');
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

  
}