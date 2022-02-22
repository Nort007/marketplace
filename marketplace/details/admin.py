from django.contrib import admin
from .models import ColorModel, SizeModel, DetailModel


@admin.register(SizeModel)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category_id', 'category', 'size']


@admin.register(ColorModel)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'color']


@admin.register(DetailModel)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'product_id', 'color', 'color_id', 'size', 'size_id', 'quantity']
