
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomeUser(AbstractUser):
    username = None
    Image=models.ImageField(upload_to='Users/images/',blank=True,null=True)
    mobile=models.CharField(_("Phone Number"),unique=True,max_length=14)
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    class Meta:
        verbose_name = "کاربران"
        verbose_name_plural="کاربران"

    def __str__(self):
        return self.mobile


