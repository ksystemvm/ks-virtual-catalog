from rest_framework import serializers
from .models import (
    Unidad, 
    UnidadDetalle, 
    Producto, 
    Presentacion, 
    VarianteGrupo, 
    VarianteGrupoValor, 
    Variante
)

# --- SERIALIZADORES DE UNIDADES ---
class UnidadDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDetalle
        fields = '__all__'

class UnidadSerializer(serializers.ModelSerializer):
    detalles = UnidadDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Unidad
        fields = ['id', 'nombre', 'detalles']


# --- SERIALIZADORES DE VARIANTES Y ATRIBUTOS ---
class VarianteGrupoValorSerializer(serializers.ModelSerializer):
    grupo_nombre = serializers.ReadOnlyField(source='grupo.nombre')

    class Meta:
        model = VarianteGrupoValor
        fields = ['id', 'grupo', 'grupo_nombre', 'valor', 'identificador']

class VarianteGrupoSerializer(serializers.ModelSerializer):
    valores = VarianteGrupoValorSerializer(many=True, read_only=True)

    class Meta:
        model = VarianteGrupo
        fields = ['id', 'nombre', 'valores']

class VarianteSerializer(serializers.ModelSerializer):
    # 'valores_detalle' devolverá los datos completos para lectura en Angular
    valores_detalle = VarianteGrupoValorSerializer(source='valores', many=True, read_only=True)

    class Meta:
        model = Variante
        fields = ['id', 'producto', 'valores', 'valores_detalle', 'modelo', 'referencia', 'precio', 'stock_disponible']


# --- SERIALIZADORES DE PRESENTACIONES Y PRODUCTO PRINCIPAL ---
class PresentacionSerializer(serializers.ModelSerializer):
    unidad_detalle = UnidadDetalleSerializer(source='unidad', read_only=True)

    class Meta:
        model = Presentacion
        fields = ['id', 'producto', 'unidad', 'unidad_detalle']

class ProductoSerializer(serializers.ModelSerializer):
    # Anidamos las variantes y presentaciones asociadas para obtener todo en un solo GET
    variantes = VarianteSerializer(many=True, read_only=True)
    presentaciones = PresentacionSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion', 'variantes', 'presentaciones']