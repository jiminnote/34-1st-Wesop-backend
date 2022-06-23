from django.urls   import path
from product.views import PerfumeView,CategoryView

urlpatterns = [
    path('/perfume',PerfumeView.as_view()),
    path('/category',CategoryView.as_view())
]