import { Routes } from '@angular/router';
import { roleGuard } from './services/role.guard';

export const routes: Routes = [
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