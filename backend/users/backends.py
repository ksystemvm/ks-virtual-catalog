from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

# Obtenemos el modelo de usuario que esté activo en el proyecto
User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Buscamos al usuario ignorando mayúsculas/minúsculas (iexact)
            # El parámetro 'username' aquí es simplemente el texto que llega desde Angular
            user = User.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except User.DoesNotExist:
            return None

        # Si el usuario existe, verificamos la contraseña
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
            
        return None