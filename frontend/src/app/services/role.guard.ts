import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from './auth.service';

// Creamos una función que recibe los roles permitidos para una ruta específica
export const roleGuard = (allowedRoles: string[]): CanActivateFn => {
  return () => {
    const authService = inject(AuthService);
    const router = inject(Router);
    const userRole = authService.getUserRole();

    // Verificamos si el usuario tiene un rol y si ese rol está en la lista de permitidos
    if (userRole && allowedRoles.includes(userRole)) {
      return true;
    }

    // Si no tiene permiso, lo redirigimos a la página principal
    router.navigate(['/']); 
    return false;
  };
};