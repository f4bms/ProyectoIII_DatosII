import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { UserService } from '../services/user.service';
import { Router } from '@angular/router';

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

  constructor(private userService: UserService, private router: Router) {}

  onSubmit() {
    this.userService.createUsuario(this.usuario).subscribe(
      response => {
        console.log('Usuario creado:', response);
        alert('Usuario registrado exitosamente.');
        this.router.navigate(['/welcome']);
      },
      error => {
        console.error('Error al registrar usuario:', error);
        alert('Error al registrar usuario.');
      }
    );
  }
}
