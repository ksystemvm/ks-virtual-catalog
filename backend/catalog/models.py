from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=50, help_text="Ej: Unidades, Volumen, Longitud")

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return f"{self.name}"
    

class UnitDetail(models.Model):
    UNIT_TYPE_CHOICES = [
        (0, 'Unidad de Referencia'),
        (1, 'Menor que la unidad de referencia'),
        (2, 'Mayor que la unidad de referencia')
    ]
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="details")
    unit_type = models.PositiveIntegerField(choices=UNIT_TYPE_CHOICES, default=2)
    name = models.CharField(max_length=30)
    quantity = models.DecimalField(max_digits=16, decimal_places=8)

    class Meta:
        verbose_name = "Detalle de Unidad"
        verbose_name_plural = "Detalles de Unidades"

    def __str__(self):
        return f"{self.name} ({self.quantity})"
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class ProductBase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto Base"
        verbose_name_plural = "Productos Base"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}"

class ProductPresentation(models.Model):
    product = models.ForeignKey(ProductBase, related_name="presentations", on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitDetail, related_name="presentation_units", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Presentación de Producto"
        verbose_name_plural = "Presentaciones de Producto"

    def __str__(self):
        return f"{self.product.name} - {self.unit.name}"
    

class VariantGroup(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Grupo de Variantes"
        verbose_name_plural = "Grupos de Variantes"

    def __str__(self):
        return f"{self.name}"
    

class VariantGroupValue(models.Model):
    group = models.ForeignKey(VariantGroup, related_name="variant_values", on_delete=models.CASCADE)
    value = models.CharField(max_length=30)
    html_color = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = "Valor de Variante"
        verbose_name_plural = "Valores de Variantes"

    def __str__(self):
        return f"{self.group.name}: {self.value}"
    

class Product(models.Model):
    presentation = models.ForeignKey(ProductPresentation, related_name="products", on_delete=models.CASCADE)
    variants = models.ManyToManyField(VariantGroupValue, related_name="products", blank=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, unique=True, blank=True, null=True)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Producto (SKU)"
        verbose_name_plural = "Productos (SKUs)"
    
    @property
    def total_price(self):
        """Calcula el precio final sumando la presentación + el extra por variante"""
        return self.presentation.price + self.extra_price

    def __str__(self):
        variants_str = ", ".join([f"{v.group.name}: {v.value}" for v in self.variants.all()])
        if variants_str:
            return f"{self.presentation.product.name} ({self.presentation.unit.name}) - [{variants_str}]"
        return f"{self.presentation.product.name} ({self.presentation.unit.name})"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='catalog/product/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes de Productos"

    def __str__(self):
        return f"Imagen de {self.product.presentation.product.name}"