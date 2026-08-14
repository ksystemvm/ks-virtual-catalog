from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

# Herramientas para generar tokens seguros
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .serializers import (
    RegistroSerializer, 
    SolicitarRecuperacionSerializer, 
    ConfirmarPasswordSerializer
)

User = get_user_model()

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            # 1. Guardar al usuario (inactivo)
            user = serializer.save()
            
            # 2. Generar un identificador único codificado y un token seguro
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            # 3. Construir el enlace que apuntará a tu frontend en Angular
            # (Más adelante crearemos esta ruta en Angular)
            enlace_activacion = f"http://localhost:4200/activar/{uid}/{token}"
            
            # 4. Preparar y enviar el correo
            asunto = 'Activa tu cuenta en Cenco Store'
            mensaje = f"""Hola {user.first_name},
            
¡Gracias por registrarte en Cenco Store! 
Por favor, haz clic en el siguiente enlace para activar tu cuenta:

{enlace_activacion}

Si no solicitaste este registro, ignora este correo.
"""
            send_mail(
                asunto, 
                mensaje, 
                settings.DEFAULT_FROM_EMAIL, 
                [user.email],
                fail_silently=False
            )
            
            return Response(
                {'mensaje': 'Usuario registrado con éxito. Revisa tu correo para activar la cuenta.'}, 
                status=status.HTTP_201_CREATED
            )
            
        # Si los datos no son válidos (ej. el correo ya existe)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivarCuentaView(APIView):
    def get(self, request, uidb64, token):
        try:
            # Descodificar el ID del usuario
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        # Verificar si el usuario existe y si el token es válido
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'mensaje': '¡Tu cuenta ha sido activada exitosamente! Ya puedes iniciar sesión.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'El enlace de activación es inválido o ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)

class SolicitarRecuperacionPasswordView(APIView):
    def post(self, request):
        serializer = SolicitarRecuperacionSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            try:
                user = User.objects.get(email__iexact=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                
                enlace_recuperacion = f"http://localhost:4200/restablecer-password/{uid}/{token}"
                
                asunto = 'Restablecer Contraseña - Cenco Store'
                mensaje = f"""Hola {user.first_name or user.username},

Hemos recibido una solicitud para restablecer la contraseña de tu cuenta en Cenco Store.
Haz clic en el siguiente enlace para ingresar tu nueva clave:

{enlace_recuperacion}

Si no solicitaste este cambio, puedes ignorar este mensaje de forma segura.
"""
                send_mail(asunto, mensaje, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
            except User.DoesNotExist:
                # Buena práctica de seguridad: No revelar si el correo existe o no en la BD
                pass

            return Response(
                {'mensaje': 'Si el correo está registrado en nuestro sistema, recibirás un enlace de recuperación.'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmarRestablecerPasswordView(APIView):
    def post(self, request):
        serializer = ConfirmarPasswordSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = serializer.validated_data['uidb64']
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']

            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            # Validar token
            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(password)  # Encripta y actualiza la contraseña
                user.save()
                return Response(
                    {'mensaje': '¡Contraseña actualizada con éxito! Ya puedes iniciar sesión con tu nueva clave.'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'El enlace de recuperación es inválido o ha expirado.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)