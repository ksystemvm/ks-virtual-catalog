import { Routes } from '@angular/router';
import { roleGuard } from './services/role.guard';

export const routes: Routes = [
  {
    path: 'login', 
    loadComponent: () => import('./features/auth/login/login.component').then(m => m.LoginComponent), 
  },
  {
    path: 'signup', 
    loadComponent: () => import('./features/auth/register/register.component').then(m => m.AuthRegisterComponent), 
  },
  {
    path: 'reset-password', 
    loadComponent: () => import('./features/auth/reset-password/reset-password.component').then(m => m.AuthResetPasswordComponent), 
  },
  // { 
  //   path: '', 
  //   component: CatalogoPublicoComponent // Acceso libre
  // },
  // { 
  //   path: 'pedidos', 
  //   component: PedidosComponent,
  //   // Solo Supervisores y Admins pueden entrar a gestionar pedidos generales
  //   canActivate: [roleGuard(['SUPERVISOR', 'ADMIN'])] 
  // },
  // { 
  //   path: 'admin', 
  //   component: PanelAdminComponent,
  //   // Acceso ultra restringido
  //   canActivate: [roleGuard(['ADMIN'])] 
  // }
];