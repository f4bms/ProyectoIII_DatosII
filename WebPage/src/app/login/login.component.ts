import {FormsModule} from '@angular/forms';
import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import {Router} from '@angular/router';
import Swal from 'sweetalert2'

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


        Swal.fire({
          title: 'Bienvenido!',
          text: 'Bienvenido, ' + response.usuario[1],
          icon: 'success',
          confirmButtonText: 'Empieza a navegar'
        })
        this.router.navigate(['/welcome']);
      },
      (      error: any) => {
        Swal.fire({
          title: 'Algo salio mal!',
          text: 'Correo o contraseña incorrectos.',
          icon: 'error',
          confirmButtonText: 'Intenta de nuevo'
        })
      }
    );
  }
}
