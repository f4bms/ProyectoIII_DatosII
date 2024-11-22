import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient, private auth: AuthService) {}

  getAllUsuarios(): Observable<any> {
    return this.http.get(`${this.apiUrl}/usuarios`);
  }

  async createUsuario(usuario: any): Promise<Observable<any>> {
    try {
      usuario['contrasena'] = this.auth.hashData(usuario['contrasena'])
      const encryptedData = await this.auth.encryptData(usuario);
      return this.http.post(`${this.apiUrl}/usuarios`, { data: encryptedData });
    } catch (error) {
      console.error('Error al encriptar los datos:', error);
      throw error;
    }
  }
  

  async login(correo: string, contrasena: string): Promise<Observable<any>> {


    try {
      contrasena = this.auth.hashData(contrasena)
      const encryptedData = await this.auth.encryptData({ correo, contrasena });
      return this.http.post(`${this.apiUrl}/login`, { data: encryptedData });
    } catch (error) {
      console.error('Error al encriptar los datos:', error);
      throw error;
    }

    
  }
}
