from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):
    """
    Permiso exclusivo para usuarios con rol ADMINISTRADOR.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'ADMIN'
        )


class IsSupervisorRole(permissions.BasePermission):
    """
    Permiso para usuarios con rol SUPERVISOR o ADMINISTRADOR.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['SUPERVISOR', 'ADMIN']
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    PERMISO PARA EL CATÁLOGO PÚBLICO:
    - Cualquier usuario (incluso anónimo/sin iniciar sesión) puede VER los productos (GET, HEAD, OPTIONS).
    - Solo los usuarios con rol ADMINISTRADOR pueden CREAR, EDITAR o ELIMINAR productos (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        # request.method SAFE_METHODS engloba ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True  # Acceso libre sin necesidad de login
        
        # Para peticiones de modificación, exigimos estar autenticado y ser ADMIN
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'ADMIN'
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
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Admin y Supervisor pueden ver y editar cualquier pedido
        if request.user.role in ['ADMIN', 'SUPERVISOR']:
            return True
        # El cliente solo puede ver o consultar su propio pedido
        return obj.cliente == request.user