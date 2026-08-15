import { Component, inject } from '@angular/core';
import { Router, RouterModule } from '@angular/router'; // <-- RouterModule para usar routerLink
import { FormsModule } from '@angular/forms'; // <-- Importamos FormsModule para [(ngModel)]
import { CommonModule } from '@angular/common'; // <-- Importamos CommonModule para *ngIf
import { AuthService } from '../../../services/auth.service'; 

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [
    FormsModule, 
    CommonModule, 
    RouterModule
  ] 
})
export class LoginComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  identificador = '';
  password = '';
  mensajeError = '';
  cargando = false;

  iniciarSesion() {
    if (!this.identificador || !this.password) {
      this.mensajeError = 'Por favor, completa todos los campos.';
      return;
    }

    this.cargando = true;
    this.mensajeError = '';

    this.authService.login({ username: this.identificador, password: this.password })
      .subscribe({
        next: () => {
          this.cargando = false;
          const rol = this.authService.getUserRole();
          
          if (rol === 'ADMIN') {
            this.router.navigate(['/admin']);
          } else if (rol === 'SUPERVISOR') {
            this.router.navigate(['/pedidos']);
          } else {
            this.router.navigate(['/']);
          }
        },
        error: (err) => {
          this.cargando = false;
          this.mensajeError = 'Usuario, correo o contraseña incorrectos.';
          console.error(err);
        }
      });
  }
}