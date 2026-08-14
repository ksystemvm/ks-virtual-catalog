"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.core.management import call_command
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth.models import User
from users.models import CustomUser
from users.serializers import CustomTokenObtainPairSerializer

def setup_superuser(request):
    if not CustomUser.objects.filter(username='ksystem').exists():
        CustomUser.objects.create_superuser(
            username='ksystem', 
            email='ksystem.vm@gmail.com', 
            password='18298561.vm'
        )
        return HttpResponse("¡Excelente! Superusuario creado con éxito.")
    return HttpResponse("El superusuario ya existe. No se realizó ninguna acción.")
    
def generar_estilos(request):
    try:
        call_command('collectstatic', interactive=False)
        return HttpResponse("¡Magia lista! Archivos estáticos recolectados.")
    except Exception as e:
        return HttpResponse(f"Hubo un error: {str(e)}")

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/records/', include('records.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/auth/'), include('users.urls'),

    # Ruta secreta temporal
    # ---------------------
    path('create-superuser/', setup_superuser),
    # path('setup-styles/', generar_estilos),
]

