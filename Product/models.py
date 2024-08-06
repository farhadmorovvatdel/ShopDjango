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
    name = models.CharField(max_length=50,verbose_name='نام محصول')
    description = models.TextField(blank=True, null=True,verbose_name='توضیحات')
    base_price = models.PositiveSmallIntegerField(verbose_name='قیمت محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='دسته بندی محصول')
    Image=models.ImageField(upload_to="Products/Images",null=True,blank=True,verbose_name='عکس محصول')
    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE,verbose_name='نام محصول')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,verbose_name='رنگ محصول')
    size = models.ForeignKey(Size, on_delete=models.CASCADE,verbose_name='سایز محصول')


    class Meta:
        verbose_name = "ویژگی محصول"
        verbose_name_plural = " ویژگی محصولات"
    def __str__(self):
        return f'{self.product.name} - {self.color.color_name} - {self.size.name}'
class Faviorate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites',verbose_name="نام محصول")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_favorite')
        ]
        verbose_name="علاقه مندی"
        verbose_name_plural="علاقه مندی ها"
