from django.db.models import Model, DateTimeField, CharField
from django.utils import timezone
from datetime import datetime


class BaseModel(Model):
    """Базовая модель ко всем таблицам"""
    created_at: datetime = DateTimeField(db_index=True, default=timezone.now)
    updated_at: datetime = DateTimeField(auto_now=True)

    class Meta:
        """Является абстрактным.
        Т.Е. применяется к таблицам,
        но не добавляется таблицей в бд
        https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
        https://django.fun/docs/django/ru/3.2/topics/db/models/#abstract-base-classes"""
        abstract = True


class CountryModel(BaseModel, Model):
    """pass"""
    name = CharField(max_length=64, null=False)
    country_code = CharField(max_length=8, null=False)

    class Meta:
        """pass"""
        db_table = "countries"

    def __str__(self):
        return self.name