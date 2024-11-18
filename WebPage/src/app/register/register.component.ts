import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [
    FormsModule
  ],
  standalone: true
})
export class RegisterComponent {
  usuario = {
    nombre_completo: '',
    nombre_usuario: '',
    correo: '',
    contrasena: '',
    telefono: ''
  };

  constructor(private userService: UserService) {}

  onSubmit() {
    this.userService.createUsuario(this.usuario).subscribe(
      response => {
        console.log('Usuario creado:', response);
        alert('Usuario registrado exitosamente.');
      },
      error => {
        console.error('Error al registrar usuario:', error);
        alert('Error al registrar usuario.');
      }
    );
  }
}
