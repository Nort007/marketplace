"""Файл описывает подготовительный контент
input/output данных"""
import django_filters.rest_framework
from .models import ProductModel, CategoryModel
from rest_framework.response import Response
from .selectors import get_all_categories, product_list, product_detail_list
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import generics
from .pagination import LimitOffsetPagination, get_paginated_response
from details.models import DetailModel

from itertools import chain

class CategoryApi(APIView):
    """Возвращает полный список категории каталога"""
    class OutputSerializer(serializers.ModelSerializer):
        """Дессериализует данные с нужными полями"""
        class Meta:
            """https://docs.djangoproject.com/en/4.0/ref/models/options/"""
            model = CategoryModel
            fields = ('id', 'name', )

    def get(self, request):
        categories = get_all_categories()
        data = self.OutputSerializer(categories, many=True).data
        return Response(
            {
                "status": Response.status_code,
                "categories": data,
            }
        )


class ProductApi(APIView):
    """Получить продукт по фильтрам или все продукты сразу"""
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class FilterSerializer(serializers.Serializer):
        """Фильтрует полученный запрос по key-value
        переменные класса - это key для фильтра"""
        id = serializers.IntegerField(required=False)
        name = serializers.CharField(required=False)
        category = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source='category.name', read_only=True)
        manufacturer = serializers.CharField(source='manufacturer.name', read_only=True)
        description = serializers.CharField(source='description.description', read_only=True)

        class Meta:
            model = ProductModel
            fields = "__all__"


    def get(self, request):
        """https://www.django-rest-framework.org/api-guide/requests/#query_params"""
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        product = product_list(filters=filter_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=product,
            request=request,
            view=self
        )


class ProductDetailApi(APIView):
    """Отвечает детальными данными по выбранному продукту"""

    class FilterSerializer(serializers.Serializer):
        """Фильтр по каким атрибутам доступна сериализация, иначе фильтр для поиска"""
        product = serializers.CharField(required=False)
        color = serializers.CharField(required=False)
        size = serializers.CharField(required=False)

    class OutputSerializer(serializers.Serializer):
        """Дессериализация данных для api.
        Каким переменным будет переопределены
        значения id в наименование"""
        product = serializers.CharField(source='product.name', read_only=True)
        color = serializers.CharField(source='color.color', read_only=True)
        size = serializers.CharField(source='size.size', read_only=True)

    def get(self, request):
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        detail = product_detail_list(filters=filter_serializer.validated_data)
        print(detail)
        result = self.OutputSerializer(detail, many=True).data

        return Response({
            "result": result,
        })
