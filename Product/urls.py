from django.urls import  path
from .views import ProductDetailView,ProductFaviorate,AddProductFaviorate,DeleteProductFaviorate
app_name='Product'
urlpatterns=[
    path('detail/<int:id>/',ProductDetailView,name='ProductDetail'),
    path('wishlist',ProductFaviorate,name='Productfaviorate'),
    path("addfaviorate/<int:id>/",AddProductFaviorate,name="addfaviorate"),
    path("deletefaviorate/<int:item_id>/",DeleteProductFaviorate,name="deleteproductfaviorate")
]