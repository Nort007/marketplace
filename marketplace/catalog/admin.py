from django.contrib import admin

from .models import ManufacturerModel, CategoryModel, ProductModel, DescriptionModel


@admin.register(ManufacturerModel)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ['name  ', ]
    list_filter = ['country', ]
    list_display = ['name', 'phone', 'country', 'address']

    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model._default_manager.get_query_set()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)

        # Custom Search
        # 1. Get the query value and clear it from the request
        q = ''
        try:
            q = request.GET['q']
            copy = request.GET.__copy__()
            copy.__delitem__('q')
            request.GET = copy

        except:
            pass

        result_list = []

        # Search on main model (Person)
        person_obj_list = ManufacturerModel.objects.filter(name__contains=q)
        for person in person_obj_list:
            result_list.append(person.pk)
        return qs.filter(pk__in=result_list)  # apply the filter


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'all_quantity', 'available', 'manufacturer', 'manufacturer_id', 'category', 'category_id', 'description_id']


@admin.register(DescriptionModel)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']