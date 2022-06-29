from django.urls import path
from product.views import ProductListView,CategoryView

urlpatterns = [
    path('/categories',CategoryView.as_view()),
    path('', ProductListView.as_view())
]


