from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductBaseViewSet, ProductViewSet,
    ProductPresentationViewSet,
    UnitViewSet, UnitDetailViewSet, VariantGroupViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products-base', ProductBaseViewSet)
router.register(r'products-skus', ProductViewSet)
router.register(r'presentations', ProductPresentationViewSet)
router.register(r'units', UnitViewSet)
router.register(r'unit-details', UnitDetailViewSet)
router.register(r'variant-groups', VariantGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]