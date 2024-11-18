import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Redirige a 'home'
  { path: 'home', component: HomeComponent }, // Ruta para Home
  { path: 'login', component: LoginComponent }, // Ruta para Login
  { path: 'register', component: RegisterComponent } // Ruta para Registro
];
