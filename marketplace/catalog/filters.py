import django_filters
from .models import ProductModel
from details.models import DetailModel
from rest_framework import serializers

class ProductModelFilter(django_filters.FilterSet):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'category', )


class ProductDetailModelFilter(django_filters.FilterSet):
    class Meta:
        model = DetailModel
        fields = ('product', 'color', 'size', )
