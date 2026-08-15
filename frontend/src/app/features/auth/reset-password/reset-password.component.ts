import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-auth-reset-password',
  templateUrl: './reset-password.component.html',
  imports: [CommonModule, FormsModule, RouterModule]
})
export class AuthResetPasswordComponent {
  email = '';
  mensaje = '';
  cargando = false;

  enviarEnlace() {
    if (!this.email) {
      this.mensaje = 'Por favor, ingresa tu correo electrónico.';
      return;
    }

    this.cargando = true;
    this.mensaje = '';

    // Simulamos la petición al backend
    setTimeout(() => {
      this.cargando = false;
      this.mensaje = 'Si el correo existe en nuestra base de datos, recibirás un enlace para restablecer tu contraseña en los próximos minutos.';
      this.email = '';
    }, 1500);
  }
}