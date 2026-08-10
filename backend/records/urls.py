# records/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'currencies', views.CurrencyViewSet)
router.register(r'exchange-rates', views.ExchangeRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]