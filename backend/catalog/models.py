from django.db import models

class Unidad(models.Model):
    nombre = models.CharField(max_length=50, help_text="Ej: Unidades, Volumen, Longitud")

    def __str__(self):
        return f"{self.nombre}"

class UnidadDetalle(models.Model):
    TIPO_UNIDAD = [
        (0, 'Unidad de Referencia'),
        (1, 'Menor que la unidad de referencia'),
        (2, 'Mayor que la unidad de referencia')
    ]
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name="detalles")
    tipo_unidad = models.PositiveIntegerField(choices=TIPO_UNIDAD, default=2)
    presentacion = models.CharField(max_length=30)
    cantidad_por_presentacion = models.DecimalField(max_digits=16, decimal_places=8)

    def __str__(self):
        return f"{self.presentacion} ({self.cantidad_por_presentacion})"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"

class Presentacion(models.Model):
    producto = models.ForeignKey(Producto, related_name="presentaciones", on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadDetalle, related_name="unidad_presentacion", on_delete=models.CASCADE)
    precio_presentacion = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.unidad.presentacion}"

class VarianteGrupo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class VarianteGrupoValor(models.Model):
    grupo = models.ForeignKey(VarianteGrupo, related_name="valores", on_delete=models.CASCADE)
    valor = models.CharField(max_length=30)
    identificador = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.grupo.nombre}: {self.valor}"

class Variante(models.Model):
    producto = models.ForeignKey(Producto, related_name="variantes", on_delete=models.CASCADE)
    variante = models.ManyToManyField(VarianteGrupoValor, related_name="variantes", blank=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, unique=True, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        variante = ""
        if self.variante:
            variante = f" - {self.variante.grupo.nombre}: {self.variante.valor}"
        return f"{self.producto.nombre}{variante}"

