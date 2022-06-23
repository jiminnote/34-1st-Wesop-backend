from lib2to3.refactor import MultiprocessRefactoringTool
from unittest import result
from django.http   import JsonResponse
from django.views  import View

from core.utils      import login_decorator
from product.models  import *

class PerfumeView(View):
    def get(self, request):
        # main_category = MainCategory.objects.get(id=4)
        perfume=[{
        "id"                 : product.id,
        "name"               : product.name, 
        "additional_content" : product.additional_content,
        "image_url" : [
                    {
                        'id'   : .id,
                        'name' : .name
                    } 
                ] 
        } for product in Product.objects.get(id=4)]
        
        
        return JsonResponse({'perfume':perfume}, status=200)
    
 