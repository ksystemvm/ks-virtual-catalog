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

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer

class VarianteViewSet(viewsets.ModelViewSet):
    queryset = Variante.objects.all()
    serializer_class = VarianteSerializer

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