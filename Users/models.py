import jdatetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomeUser(AbstractUser):
    username = None
    Image=models.ImageField(upload_to='Users/images/',blank=True,null=True)
    mobile=models.CharField(("موبایل"),unique=True,max_length=11,)
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    class Meta:
        verbose_name = "کاربران"
        verbose_name_plural="کاربران"

    def __str__(self):
        return self.mobile

    # def get_jalali_date(self):
    #     return jdatetime.date.fromgregorian(date_joined=self.date_joined).strftime('%Y/%m/%d')


