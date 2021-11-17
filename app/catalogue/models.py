from django.db import models
from django.utils.text import slugify

class ProductVariant(models.Model):
    name = models.CharField(max_length=256)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='products')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=256)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    item = models.CharField(max_length=256)
    product_id = models.CharField("Product ID",null=True, blank=True, max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='category')

    def __str__(self):
        return self.item
