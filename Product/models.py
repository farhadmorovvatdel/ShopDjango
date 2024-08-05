from django.db import models
from Category.models import Category
from DjangoProjectShop import settings


class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    color_name=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"
class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایز"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)

    description = models.TextField(blank=True, null=True)
    base_price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="Products/Images",null=True,blank=True)
    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "ویژگی محصول"
        verbose_name_plural = " ویژگی محصولات"
    def __str__(self):
        return f'{self.product.name} - {self.color.color_name} - {self.size.name}'
class Faviorate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_favorite')
        ]