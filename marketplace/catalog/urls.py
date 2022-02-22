from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.CategoryApi.as_view()),
    path('products/', views.ProductApi.as_view()),
    path('product-detail/', views.ProductDetailApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
