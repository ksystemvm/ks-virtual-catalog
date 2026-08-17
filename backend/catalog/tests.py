from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Category

User = get_user_model()

class RolePermissionTests(APITestCase):
    def setUp(self):
        # 1. Crear usuarios de prueba con los diferentes roles
        self.admin = User.objects.create_user(username='admin', password='123', role='ADMIN')
        self.manager = User.objects.create_user(username='manager', password='123', role='MANAGER')
        self.customer = User.objects.create_user(username='customer', password='123', role='CUSTOMER')

        # 2. Crear datos base necesarios para las pruebas
        self.category = Category.objects.create(name="Oficina", slug="oficina")

    def test_customer_readonly_access(self):
        """Un CUSTOMER solo puede leer, no puede crear categorías."""
        self.client.force_authenticate(user=self.customer)
        response = self.client.post('/api/catalog/categories/', {"name": "Nueva", "slug": "nueva"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_manager_cannot_create_category(self):
        """Un MANAGER NO debe poder crear una Categoría."""
        self.client.force_authenticate(user=self.manager)
        response = self.client.post('/api/catalog/categories/', {"name": "Papeleria", "slug": "papeleria"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_manager_can_create_product_base(self):
        """Un MANAGER SÍ debe poder crear un Producto Base."""
        self.client.force_authenticate(user=self.manager)
        data = {
            "category": self.category.id,
            "name": "Cuaderno Profesional",
            "slug": "cuaderno-profesional"
        }
        response = self.client.post('/api/catalog/products-base/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_can_create_category(self):
        """Un ADMIN debe tener control total y crear categorías."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/catalog/categories/', {"name": "Escolar", "slug": "escolar"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)