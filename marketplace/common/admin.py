from django.contrib import admin

from .models import CountryModel


@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'country_code']