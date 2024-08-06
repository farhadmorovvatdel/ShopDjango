import jdatetime
from django.contrib import admin
from .models import Product,Size,Color,ProductVariation,Faviorate

admin.site.register(Size)
admin.site.register(Color)



class FaviorateAdmin(admin.ModelAdmin):
    def show_fullname(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}' if obj.user.first_name and obj.user.last_name else "-"

    def date_shamsi(self,obj):
        jalali_date=jdatetime.datetime.fromgregorian(datetime=obj.created_at)
        return jalali_date.strftime('%H:%M:%S %Y-%m-%d ')

    show_fullname.short_description = 'نام و نام خانوادگی'
    date_shamsi.short_description = "تاریخ ایجاد"
    list_display = ['product','show_fullname','date_shamsi']

admin.site.register(Faviorate,FaviorateAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['product','color','size']


admin.site.register(ProductVariation,ProductVariationAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','base_price','category']


admin.site.register(Product,ProductAdmin)
