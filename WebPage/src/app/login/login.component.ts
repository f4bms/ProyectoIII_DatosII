import {FormsModule} from '@angular/forms';
import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [
    FormsModule
  ],
  standalone: true
})
export class LoginComponent {
  loginData = {
    correo: '',
    contrasena: ''
  };

  constructor(private userService: UserService) {}

  onLogin() {
    this.userService.login(this.loginData.correo, this.loginData.contrasena).subscribe(
      response => {
        console.log('Inicio de sesión exitoso:', response);
        alert('Bienvenido, ' + response.usuario[1]); // Supone que el nombre completo está en la posición 1
      },
      error => {
        console.error('Error al iniciar sesión:', error);
        alert('Correo o contraseña incorrectos.');
      }
    );
  }
}
