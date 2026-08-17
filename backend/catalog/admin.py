from django.contrib import admin
from .models import (
    Unit, UnitDetail, Category, ProductBase, 
    ProductPresentation, VariantGroup, VariantGroupValue, 
    Product, ProductImage
)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UnitDetail)
class UnitDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'unit_type', 'quantity']
    list_filter = ['unit', 'unit_type']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

class ProductPresentationInline(admin.TabularInline):
    model = ProductPresentation
    extra = 1

@admin.register(ProductBase)
class ProductBaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductPresentationInline]

@admin.register(VariantGroup)
class VariantGroupAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(VariantGroupValue)
class VariantGroupValueAdmin(admin.ModelAdmin):
    list_display = ['group', 'value', 'html_color']
    list_filter = ['group']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['presentation', 'reference', 'model', 'extra_price', 'total_price', 'stock']
    search_fields = ['reference', 'model']
    inlines = [ProductImageInline]