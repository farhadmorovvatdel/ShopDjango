from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    parent=models.ForeignKey('Category', on_delete=models.CASCADE,
        related_name='subcategories', blank=True, null=True,verbose_name="زیر مجموعه")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی"
