import json
import random

from django.http      import JsonResponse
from django.views     import View

from product.models   import Product
class RecommendproductView(View):
    def get(self, request):
        products = Product.objects.all()
        
        randomproduct = [random.choice(products) for i in range(7)]


        results=[{
        "id"         : product.id,
        "name"       : product.name, 
        "content"    : product.Products_feature.first().content,
        "image_url"  : product.productoption_set.first().image_url
        } for product in randomproduct ]


        return JsonResponse({'perfume':results}, status=200)