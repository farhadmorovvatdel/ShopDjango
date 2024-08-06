from django.contrib import admin
from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)



admin.site.register(Category,CategoryAdmin)
