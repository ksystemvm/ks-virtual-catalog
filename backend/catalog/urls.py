from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoViewSet,
    VarianteViewSet,
    PresentacionViewSet,
    UnidadViewSet,
    UnidadDetalleViewSet,
    VarianteGrupoViewSet,
    VarianteGrupoValorViewSet
)

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'variantes', VarianteViewSet)
router.register(r'presentaciones', PresentacionViewSet)
router.register(r'unidades', UnidadViewSet)
router.register(r'unidades-detalle', UnidadDetalleViewSet)
router.register(r'grupos-variantes', VarianteGrupoViewSet)
router.register(r'valores-variantes', VarianteGrupoValorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]