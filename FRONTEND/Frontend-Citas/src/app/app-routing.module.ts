import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from '../service/auth.guard';
import { IndexComponent } from './index/index.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { RegistroComponent } from './registro/registro.component';
import { ReservarcitaComponent } from './reservarcita/reservarcita.component';
import { MiperfilComponent } from './miperfil/miperfil.component';


const routes: Routes = [
  {path: 'index', component: IndexComponent },
  {path: 'login', component: LoginComponent},
  {path: 'registro', component: RegistroComponent},
  {path: 'home', component: HomeComponent, canActivate: [AuthGuard]},
  {path: 'reservarcita', component: ReservarcitaComponent, canActivate: [AuthGuard]},
  {path: 'miperfil', component: MiperfilComponent, canActivate: [AuthGuard]},
  { path: '', redirectTo: '/index', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
