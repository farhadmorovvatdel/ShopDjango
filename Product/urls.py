from django.urls import  path
from .views import ProductDetailView
app_name='Product'
urlpatterns=[
    path('detail/<int:id>/',ProductDetailView,name='ProductDetail')
]