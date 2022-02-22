from django.db.models import Model, CharField, IntegerField, ForeignKey, PROTECT
from common.models import BaseModel
from catalog.models import CategoryModel, ProductModel


class SizeModel(BaseModel, Model):
    """Класс описывает модель таблицы всех размеров
    для всех типов одежды"""
    category: int = ForeignKey(CategoryModel, on_delete=PROTECT, db_column='category_id')
    size: str = CharField(max_length=32, null=False, default=0)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        # return str(self.pk)
        return str(self.size)


class ColorModel(BaseModel, Model):
    """Класс-модель описывает цвета,
    которые принадлежат товарам"""
    color: str = CharField(max_length=32, null=False)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return "({}){}".format(self.pk, self.color)


class DetailModel(BaseModel, Model):
    """Класс-модель описывает детальные данные о товаре"""
    product: int = ForeignKey(ProductModel, on_delete=PROTECT, db_column='product_id')
    color: int = ForeignKey(ColorModel, on_delete=PROTECT, db_column='color_id')
    size: int = ForeignKey(SizeModel, on_delete=PROTECT, db_column='size_id')
    quantity: int = IntegerField()

    class Meta:
        db_table = 'details_products'
