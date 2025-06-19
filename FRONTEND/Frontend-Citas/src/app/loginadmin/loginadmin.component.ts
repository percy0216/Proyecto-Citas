import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-loginadmin',
  standalone: false,
  templateUrl: './loginadmin.component.html',
  styleUrl: './loginadmin.component.css'
})
export class LoginadminComponent {

  constructor(private auth: AuthService, private router: Router) {}

  cerrarSesion() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }
}
