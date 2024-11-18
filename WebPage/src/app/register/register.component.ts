import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [FormsModule]
})
export class RegisterComponent {
  usuario = {
    nombre_completo: '',
    nombre_usuario: '',
    correo: '',
    contrasena: '',
    telefono: ''
  };

  onSubmit() {
    console.log('Usuario registrado:', this.usuario);
    //enviar los datos al backend
  }
}
