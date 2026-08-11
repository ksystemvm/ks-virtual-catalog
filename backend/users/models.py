from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Modelo de usuario extendido para manejar roles en el catálogo virtual.
    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Administrador')
        SUPERVISOR = 'SUPERVISOR', _('Supervisor / Vendedor')
        CLIENTE = 'CLIENTE', _('Usuario Final / Cliente')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENTE,
        verbose_name=_('Rol de Usuario')
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"