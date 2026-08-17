from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Modelo de usuario extendido para manejar roles en el catálogo virtual.
    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Administrador')
        MANAGER = 'MANAGER', _('Vendedor')
        CUSTOMER = 'CUSTOMER', _('Cliente')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
        verbose_name=_('Rol de Usuario')
    )

    is_email_verified = models.BooleanField(
        default=False,
        verbose_name="Correo Verificado",
        help_text="Indica si el usuario ha activado su cuenta mediante el enlace enviado a su correo."
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER

    @property
    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"