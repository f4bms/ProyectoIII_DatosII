import {FormsModule} from '@angular/forms';
import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  standalone: true,
  imports: [
    FormsModule
  ],
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginData = {
    correo: '',
    contrasena: ''
  };

  onLogin() {
    console.log('Datos de inicio de sesión:', this.loginData);
    // Enviar los datos al backend para autenticación
  }
}
