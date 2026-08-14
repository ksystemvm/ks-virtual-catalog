from django.urls import path
from .views import (
    RegistroUsuarioView, 
    ActivarCuentaView,
    SolicitarRecuperacionPasswordView,
    ConfirmarRestablecerPasswordView
)
urlpatterns = [
    path('register/', RegistroUsuarioView.as_view(), name='auth-register'),
    path('activate/<str:uidb64>/<str:token>/', ActivarCuentaView.as_view(), name='auth-activate'),
    path('request-password-reset/', SolicitarRecuperacionPasswordView.as_view(), name='auth-request-password-reset'),
    path('reset-password/', ConfirmarRestablecerPasswordView.as_view(), name='auth-reset-password'),
]