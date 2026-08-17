from rest_framework import serializers
from .models import (
    Unit, UnitDetail, Category, ProductBase,
    ProductPresentation, VariantGroup, VariantGroupValue,
    Product, ProductImage
)


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class UnitDetailSerializer(serializers.ModelSerializer):
    unit_name = serializers.ReadOnlyField(source='unit.name')
    unit_type_display = serializers.CharField(source='get_unit_type_display', read_only=True)

    class Meta:
        model = UnitDetail
        fields = ['id', 'unit', 'unit_name', 'unit_type', 'unit_type_display', 'name', 'quantity']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class VariantGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantGroup
        fields = ['id', 'name']


class VariantGroupValueSerializer(serializers.ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = VariantGroupValue
        fields = ['id', 'group', 'group_name', 'value', 'html_color']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    variants = VariantGroupValueSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    presentation_name = serializers.ReadOnlyField(source='presentation.unit.name')
    base_product_name = serializers.ReadOnlyField(source='presentation.product.name')

    class Meta:
        model = Product
        fields = [
            'id', 'presentation', 'base_product_name', 'presentation_name',
            'variants', 'model', 'reference', 'extra_price',
            'total_price', 'stock', 'images'
        ]


class ProductPresentationSerializer(serializers.ModelSerializer):
    unit = UnitDetailSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProductPresentation
        fields = ['id', 'product', 'unit', 'price', 'products']


class ProductBaseSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    presentations = ProductPresentationSerializer(many=True, read_only=True)

    class Meta:
        model = ProductBase
        fields = [
            'id', 'category', 'category_name', 'name',
            'slug', 'description', 'presentations',
            'created_at', 'updated_at'
        ]