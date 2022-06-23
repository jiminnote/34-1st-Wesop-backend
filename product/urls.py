from django.urls import path
from product.views import PerfumeView

urlpatterns = [
    path('/perfume',PerfumeView.as_view())
]