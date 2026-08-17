from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):
    """
    Permiso exclusivo para Administradores (Control Total).
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.is_admin
        )


class IsManagerOrAdminRole(permissions.BasePermission):
    """
    Permite lectura/edición a MANAGERs (sin eliminar).
    Otorga control total si el usuario es ADMIN.
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if request.user.is_admin:
            return True

        if request.user.is_manager:
            if request.method in ['DELETE']:
                return False
            return True

        return False

class IsReadOnlyOrAuthenticatedCustomer(permissions.BasePermission):
    """
    PERMISO PARA EL CATÁLOGO PÚBLICO:
    - Cualquier usuario (incluso anónimo/sin iniciar sesión) puede VER los productos (GET, HEAD, OPTIONS).
    - Solo los usuarios con rol ADMINISTRADOR pueden CREAR, EDITAR o ELIMINAR productos (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True  
        
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.is_email_verified
        )


class IsOrderPermission(permissions.BasePermission):
    """
    PERMISO PARA LA GESTIÓN DE PEDIDOS:
    - Usuarios no autenticados: Sin acceso.
    - Clientes: Pueden crear sus propios pedidos y consultar únicamente los suyos.
    - Supervisores y Admins: Pueden consultar y actualizar todos los pedidos de la plataforma.
    """
    def has_permission(self, request, view):
        # Exige que al menos esté autenticado para interactuar con pedidos
        return bool(request.user and request.user.is_authenticated and request.user.is_email_verified)

    def has_object_permission(self, request, view, obj):
        # Admin y Supervisor pueden ver y editar cualquier pedido
        if request.user.role in ['ADMIN', 'MANAGER']:
            return True
        # El cliente solo puede ver o consultar su propio pedido
        return obj.cliente == request.user