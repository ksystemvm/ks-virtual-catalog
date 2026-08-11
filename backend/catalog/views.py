from rest_framework import viewsets
from .models import (
    Unidad, 
    UnidadDetalle, 
    Producto, 
    Presentacion, 
    VarianteGrupo, 
    VarianteGrupoValor, 
    Variante
)
from .serializers import (
    UnidadSerializer,
    UnidadDetalleSerializer,
    ProductoSerializer,
    PresentacionSerializer,
    VarianteGrupoSerializer,
    VarianteGrupoValorSerializer,
    VarianteSerializer
)
from users.permissions import (
    IsAdminOrReadOnly, 
    IsAdminRole,
    IsOrderPermission,
    IsSupervisorRole
)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminOrReadOnly]

class VarianteViewSet(viewsets.ModelViewSet):
    queryset = Variante.objects.all()
    serializer_class = VarianteSerializer
    permission_classes = [IsAdminOrReadOnly]

class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class UnidadDetalleViewSet(viewsets.ModelViewSet):
    queryset = UnidadDetalle.objects.all()
    serializer_class = UnidadDetalleSerializer

class VarianteGrupoViewSet(viewsets.ModelViewSet):
    queryset = VarianteGrupo.objects.all()
    serializer_class = VarianteGrupoSerializer

class VarianteGrupoValorViewSet(viewsets.ModelViewSet):
    queryset = VarianteGrupoValor.objects.all()
    serializer_class = VarianteGrupoValorSerializer

# class PedidoViewSet(viewsets.ModelViewSet):
#     serializer_class = PedidoSerializer
#     permission_classes = [IsOrderPermission]

#     def get_queryset(self):
#         user = self.request.user
        
#         # Si es Admin o Supervisor, retornamos TODOS los pedidos
#         if user.role in ['ADMIN', 'SUPERVISOR']:
#             return Pedido.objects.all()
        
#         # Si es Cliente, filtramos para que solo vea SUS propios pedidos
#         return Pedido.objects.filter(cliente=user)

