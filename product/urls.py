from django.urls import path
from product.views import RecommendproductView

urlpatterns = [
    #path('/productdetail',ProductdetailView.as_view()),
    path('/recommendproduct',RecommendproductView.as_view())
]