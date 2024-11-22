import {FormsModule} from '@angular/forms';
import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import {Router} from '@angular/router';

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

  constructor(private userService: UserService, private router: Router) {}

  async onLogin() {
    (await this.userService.login(this.loginData.correo, this.loginData.contrasena)).subscribe(
      (      response: { usuario: string[]; }) => {
        console.log('Inicio de sesión exitoso:', response);
        alert('Bienvenido, ' + response.usuario[1]);
        this.router.navigate(['/welcome']);
      },
      (      error: any) => {
        console.error('Error al iniciar sesión:', error);
        alert('Correo o contraseña incorrectos.');
      }
    );
  }
}
