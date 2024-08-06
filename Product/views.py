from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Product,ProductVariation,Faviorate
from django.shortcuts import get_object_or_404
from django.db.models import Min
from .models import Product
from django.contrib.auth.decorators import login_required
def ProductDetailView(request,id):
    product = Product.objects.filter(id=id).first()

    uniq_colors=ProductVariation.objects.filter(product=product).prefetch_related('variations').values('color').annotate(min_id=Min('id')).values('min_id')

    unique_sizes = ProductVariation.objects.filter(product=product).values('size').annotate(min_id=Min('id')).values('min_id')
    print(unique_sizes)
    unique_variations = ProductVariation.objects.filter(id__in=unique_sizes)
    unique_variation_color= ProductVariation.objects.filter(id__in=uniq_colors)

    context={
        "unique_size":unique_variations,
         "unique_variation_color": unique_variation_color,
         'product':product,

    }


    return render(request,'Product_Detail.html',context)

@login_required(login_url="/")
def ProductFaviorate(request):
    UserFaviorats=Faviorate.objects.filter(user=request.user)
    print(UserFaviorats)

    print(UserFaviorats)
    context={
        "UserFaviorats":UserFaviorats
    }
    return  render(request,"wishlist.html",context)

@login_required(login_url="/")
def AddProductFaviorate(request,id):
        product=get_object_or_404(Product,id=id)
        user=request.user
        Addfaviorate=Faviorate.objects.filter(product=product,user=user).exists()
        if Addfaviorate :
             return  JsonResponse({'status':'Found'})
        else:
            Faviorate.objects.create(product=product,user=user)
            return  JsonResponse({"status":'Added'})
        return  render(request,'wishlist.html')

def DeleteProductFaviorate(request,item_id):
    if request.method== 'POST':
        item = get_object_or_404(Faviorate, id=item_id, user=request.user)
        item.delete()
    return redirect('Product:Productfaviorate')

