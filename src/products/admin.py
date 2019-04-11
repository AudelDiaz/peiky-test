from django.contrib import admin

from products.models import Product, Variant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass
