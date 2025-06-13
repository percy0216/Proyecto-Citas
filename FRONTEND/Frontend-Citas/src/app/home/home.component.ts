import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: false,
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(private auth: AuthService, private router: Router) {}

  cerrarSesion() {
  this.auth.logout();
  this.router.navigate(['/login']);
}
}
