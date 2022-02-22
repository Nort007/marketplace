from .models import CategoryModel, ProductModel
from typing import Iterable
from .filters import ProductModelFilter, ProductDetailModelFilter
from django.db.models.query import QuerySet
from details.models import DetailModel, SizeModel, ColorModel
from rest_framework import serializers


def get_all_categories() -> Iterable[CategoryModel]:
    """Возвращает все категории для общего каталога"""
    categories = CategoryModel.objects.all()
    print(CategoryModel.objects.values_list('id', 'name'))
    return categories


def get_categories_by_name(name):
    """Возвращает категорию и ее данные в
    соответствии с данными, иначе исключение"""
    categories = CategoryModel.objects.filter(name=name)
    print(categories)
    return categories


def product_list(*, filters=None) -> QuerySet[ProductModel]:
    filters = filters or {}
    if 'category' in filters.keys():
        if isinstance(filters['category'], str) and len(filters['category']) > 1:
            cat_id = CategoryModel.objects.get(name=filters['category'].capitalize())
            filters['category'] = cat_id
        else:
            filters.pop('category')
    qs = ProductModel.objects.all()
    return ProductModelFilter(filters, qs).qs


def product_detail_list(*, filters=None) -> Iterable[DetailModel]:
    """Отдает продукты по фильтрам"""
    filters = filters or {}
    if 'size' in filters.keys():
        print(filters['size'], filters['size'].isdigit())
        if isinstance(filters['size'], str) and len(filters['size']) > 1:
            print('this field')
            try:
                size_id = SizeModel.objects.get(size=filters['size'])
                filters['size'] = size_id
            except SizeModel.DoesNotExist:
                raise serializers.ValidationError({'size': "The size doesn't exist"})
        else:
            filters.pop('size')

    if 'color' in filters.keys():
        if isinstance(filters['color'], str) and len(filters['color']) > 1:
            color_id = ColorModel.objects.get(color=filters['color'])
            filters['color'] = color_id
    if 'product' in filters.keys():
        if isinstance(filters['product'], str) and len(filters['product']) > 1:
            product_id = DetailModel.objects.get(product=filters['product'])
            filters['product'] = product_id

    qs = DetailModel.objects.all()
    return ProductDetailModelFilter(filters, qs).qs
