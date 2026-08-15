import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-auth-register',
  templateUrl: './register.component.html',
  imports: [CommonModule, FormsModule, RouterModule]
})
export class AuthRegisterComponent {
  nombre = '';
  email = '';
  password = '';
  confirmPassword = '';
  
  mensajeError = '';
  mensajeExito = '';
  cargando = false;

  registrar() {
    this.mensajeError = '';
    this.mensajeExito = '';

    if (!this.nombre || !this.email || !this.password || !this.confirmPassword) {
      this.mensajeError = 'Por favor, completa todos los campos.';
      return;
    }

    if (this.password !== this.confirmPassword) {
      this.mensajeError = 'Las contraseñas no coinciden.';
      return;
    }

    this.cargando = true;

    // Aquí irá la llamada al backend en el futuro. 
    // Por ahora simulamos una carga de 1.5 segundos.
    setTimeout(() => {
      this.cargando = false;
      this.mensajeExito = '¡Registro exitoso! Por favor revisa tu correo para activar tu cuenta.';
      
      // Limpiamos el formulario
      this.nombre = ''; this.email = ''; this.password = ''; this.confirmPassword = '';
    }, 1500);
  }
}