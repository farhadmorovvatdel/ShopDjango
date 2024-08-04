from django.shortcuts import render
from .models import Product,ProductVariation
from django.shortcuts import get_object_or_404
from django.db.models import Min, Count


def ProductDetailView(request,id):
    product = Product.objects.filter(id=id).first()
    pr=ProductVariation.objects.filter(product=product).prefetch_related('variations').values('color').annotate(min_id=Min('id')).values('min_id')
    unique_sizes = ProductVariation.objects.filter(product=product).values('size').annotate(min_id=Min('id')).values('min_id')
    unique_variations = ProductVariation.objects.filter(id__in=unique_sizes)
    uniqvariations= ProductVariation.objects.filter(id__in=pr)
    context={
        "unique_size":unique_variations,
         "uniquvariations":uniqvariations,
         'product':product,


    }




    return render(request,'Product_Detail.html',context)