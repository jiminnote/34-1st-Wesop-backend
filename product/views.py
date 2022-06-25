import json

from django.http      import JsonResponse
from django.views     import View

from product.models   import Product
class RecommendView(View):
    def get(self, request):
        products = Product.objects.filter(id__gt=15)
        # image_url=[
        #             {
        #                 'id'   : product.id,
        #                 'name' : product.name
        #             } main_sub_category
        #         ] for in 
        
        perfume=[{
        "id"                 : product.id,
        "name"               : product.name, 
        "additional_content" : product.additional_content,
        "image_url"          : product.productoption_set.get().image_url
        } for product in products]


        return JsonResponse({'perfume':perfume}, status=200)
