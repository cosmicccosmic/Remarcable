from django.contrib import admin
from .models import Category,Tag, Product

# Registered models for Django Admin usage
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
