from django.http   import JsonResponse
from django.views  import View

from core.utils      import login_decorator
from product.models  import Product,Productoption



class PerfumeView(View):
    def get(self, request):
        results=[]
        for products in Productoption.objects.all():
            results.append(
                {
                "id" :  products.product.id,
                "name" : products.product.name,
                "image_url" : products.image_url,
                "addtional_name" : products.addtional_name,
                }
            )
        return JsonResponse({'result':results}, status=200)


