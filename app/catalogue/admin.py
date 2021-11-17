from django.contrib import admin
from .models import ProductVariant, Product, Category


class ProductVariantTabularInline(admin.TabularInline):
    model = ProductVariant




class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantTabularInline]
    model = Product
    list_display = ['item', 'category']


# Register your models here.
admin.site.register(Product, ProductAdmin)