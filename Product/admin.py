from django.contrib import admin
from .models import Product,Size,Color,ProductVariation
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductVariation)

