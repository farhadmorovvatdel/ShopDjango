from django.contrib import admin
from .models import CustomeUser

class UserAdmin(admin.ModelAdmin):
    def show_email(self,obj):
        return obj.email if obj.email else "-"
    def show_fullname(self,obj):
        return f'{obj.first_name} {obj.last_name}' if obj.first_name and obj.last_name else "-"
    def is_active_display(self,obj):
        return obj.is_active
    def is_superuser_display(self,obj):
          return obj.is_superuser

    show_fullname.short_description = 'نام و نام خانوادگی'
    show_email.short_description = ' ایمیل'
    is_superuser_display.short_description = 'ادمین'
    is_superuser_display.boolean = True
    list_display = ('mobile','show_fullname',"show_email","is_active","is_superuser_display","date_joined","get_jalali_date")
    list_editable = ('is_active',)
    list_filter = ("mobile",)

admin.site.register(CustomeUser,UserAdmin)


