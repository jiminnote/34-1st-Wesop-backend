from django.urls import path
from product.views import RecommendView

urlpatterns = [
    #path('/productdetail',ProductdetailView.as_view()),
    path('/recommend',RecommendView.as_view())
]
