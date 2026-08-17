from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .models import (
    Unit, UnitDetail, Category, ProductBase,
    ProductPresentation, VariantGroup, VariantGroupValue,
    Product, ProductImage
)
from .serializers import (
    UnitSerializer, UnitDetailSerializer, CategorySerializer,
    ProductBaseSerializer, ProductPresentationSerializer,
    VariantGroupSerializer, VariantGroupValueSerializer,
    ProductSerializer, ProductImageSerializer
)

class CatalogAccessPermission(permissions.BasePermission):
    """
    Control de acceso basado en Roles:
    - CUSTOMER (o anónimo): Solo lectura (GET, HEAD, OPTIONS).
    - MANAGER: Lectura y Edición (PUT, PATCH) global. Creación (POST) SOLO en Productos y Presentaciones.
    - ADMIN: Control total (POST, PUT, PATCH, DELETE).
    """
    def has_permission(self, request, view):
        # 1. Acceso al Catálogo (Lectura) permitido para todos (incluye CUSTOMER)
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # 2. Para cualquier otra acción, el usuario debe estar autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # 3. ADMIN: Control total
        if getattr(request.user, 'is_admin', False) or request.user.is_superuser:
            return True

        # 4. MANAGER: Lógica condicional.
        if getattr(request.user, 'is_manager', False):
            if request.method in ['PUT', 'PATCH']:
                return True

            if request.method == 'POST':
                allowed_views = ['ProductBaseViewSet', 'ProductViewSet', 'ProductPresentationViewSet']
                if view.__class__.__name__ in allowed_views:
                    return True
                
            return False

        # Si no cumple ninguna de las anteriores, denegar acceso
        return False

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [CatalogAccessPermission]

class ProductPresentationViewSet(viewsets.ModelViewSet):
    queryset = ProductPresentation.objects.select_related('product', 'unit').all()
    serializer_class = ProductPresentationSerializer
    permission_classes = [CatalogAccessPermission]

class ProductBaseViewSet(viewsets.ModelViewSet):
    queryset = ProductBase.objects.prefetch_related(
        'presentations__unit',
        'presentations__products__variants__group',
        'presentations__products__images'
    ).select_related('category').all()
    serializer_class = ProductBaseSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['created_at', 'name']
    permission_classes = [CatalogAccessPermission]





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('presentation__product', 'presentation__unit').prefetch_related('variants', 'images').all()
    serializer_class = ProductSerializer
    search_fields = ['reference', 'model']
    permission_classes = [CatalogAccessPermission]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [CatalogAccessPermission]


class UnitDetailViewSet(viewsets.ModelViewSet):
    queryset = UnitDetail.objects.select_related('unit').all()
    serializer_class = UnitDetailSerializer
    permission_classes = [CatalogAccessPermission]


class VariantGroupViewSet(viewsets.ModelViewSet):
    queryset = VariantGroup.objects.prefetch_related('variant_values').all()
    serializer_class = VariantGroupSerializer
    permission_classes = [CatalogAccessPermission]