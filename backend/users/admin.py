from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Añadimos el campo 'role' para que sea visible y editable en el panel
    fieldsets = UserAdmin.fieldsets + (
        ('Permisos del Catálogo', {'fields': ('role',)}),
    )
    
    # Mostramos el rol como una columna principal en la lista de usuarios
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)