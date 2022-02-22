from django.db.models import (Model, TextField, FloatField,
                              IntegerField, CharField, ForeignKey, BooleanField,
                              PROTECT, )
from common.models import BaseModel, CountryModel


class ManufacturerModel(BaseModel, Model):
    """Описанная модель таблица Производителя"""

    name = CharField(max_length=128, null=False)
    phone = CharField(max_length=64, null=True, default='no phone')
    country = ForeignKey(CountryModel, on_delete=PROTECT)
    address = CharField(max_length=255, null=True, default='no address')

    class Meta:
        """pass"""
        db_table = "manufacturers"

    def __str__(self):
        return "{}: {}".format(self.name, self.country)


class CategoryModel(BaseModel, Model):
    """Описанная модель категории
    товара"""

    name = CharField(max_length=255, null=True)

    class Meta:
        """pass"""
        db_table = "categories"

    def __str__(self):
        # return str(self.pk)
        return self.name


class DescriptionModel(BaseModel, Model):
    """Описывает модель таблицы содержащую полный текст Продукта"""
    description = TextField(null=False, default='Change text')

    class Meta:
        """pass"""
        db_table = 'descriptions'

    def __str__(self):
        return str(self.pk)


class ProductModel(BaseModel, Model):
    """pass"""

    name = CharField(max_length=256, null=False)
    model = CharField(max_length=256, null=False)
    price = FloatField(default=0.0)
    available = BooleanField(default=False)
    all_quantity = IntegerField(default=0)
    short_description = CharField(max_length=256, null=False, default='change short description')
    description = ForeignKey(DescriptionModel, on_delete=PROTECT, db_column='description_id')
    manufacturer = ForeignKey(ManufacturerModel, on_delete=PROTECT, db_column='manufacturer_id')
    category = ForeignKey(CategoryModel, on_delete=PROTECT, db_column='category_id')

    class Meta:
        """pass"""
        db_table = 'products'

    def __str__(self):
        return self.name

    @property
    def detail(self):
        return "test"