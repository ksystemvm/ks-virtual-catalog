import { Component, signal, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators, AbstractControl, ValidationErrors } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../../services/auth.service';
import { email, minLength } from '@angular/forms/signals';

@Component({
  selector: 'app-auth-register',
  templateUrl: './register.component.html',
  imports: [CommonModule, ReactiveFormsModule, RouterModule]
})
export class AuthRegisterComponent {
  private authService = inject(AuthService);
  private fb = inject(FormBuilder);

  errorMessage = signal('');
  successMessage = signal('');
  isLoading = signal(false);

  registerForm = this.fb.group({
    username: ['', [Validators.required, Validators.minLength(3)]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
    confirmPassword: ['', [Validators.required]],
    firstName: [''],
    LastName: ['']
  }, { validators: this.passwordMatchValidator })

  private passwordMatchValidator(control: AbstractControl): ValidationErrors | null {
    const password = control.get('password')?.value;
    const confirmPassword = control.get('confirmPassword')?.value;
    
    if (password !== confirmPassword) {
      control.get('confirmPassword')?.setErrors({ passwordMismatch: true });
      return { passwordMismatch: true };
    }
    return null;
  }

  onSubmit() {
    this.errorMessage.set('');
    this.successMessage.set('');

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