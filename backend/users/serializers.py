from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Añadimos datos personalizados al payload del token
        token['username'] = user.username
        token['role'] = user.role  # ¡Aquí inyectamos el rol que creamos en el paso anterior!

        return token