from django.db.models import Model, CharField, FloatField, FileField, ForeignKey, PROTECT
from common.models import BaseModel
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from catalog.models import ProductModel


class BaseMediaModel(BaseModel, Model):
    """Абстрактный класс создает базовую медиа модель
    для фото/видео"""

    name = CharField(max_length=256, null=False)
    bucket_name = CharField(max_length=512, null=False)
    format = CharField(max_length=16, null=False)
    size = FloatField()

    class Meta:
        """Класс не будет создан как модель таблицы,
        а использован как модель для создания других таблиц"""
        abstract = True


class PhotoModel(BaseMediaModel, Model):
    """Описывает фото модель для таблицы в бд"""

    file = FileField(upload_to='photos/%Y/%m/%d/')

    class Meta:
        """Мета класс, указано название таблицы в бд"""
        db_table = 'photos'


class PhotosProductsModel(BaseModel, Model):
    """Класс описывает связь many-to-many
    между фото таблицей и товарной таблицей"""

    photo_id = ForeignKey(PhotoModel, on_delete=PROTECT, db_column='photo_id')
    product_id = ForeignKey(ProductModel, on_delete=PROTECT, db_column='product_id')

    class Meta:
        """pass"""
        db_table = 'photos_products'


class VideoModel(BaseMediaModel, Model):
    """Описывает видео модель для таблицы в бд"""
    file = FileField(upload_to='videos/%Y/%m/%d/')

    class Meta:
        """Мета класс, указано название таблицы в бд"""
        db_table = 'videos'


class VideosProductsModel(BaseModel, Model):
    """Класс описывает связь many-to-many
    между видео таблицей и товарной таблицей"""

    video_id = ForeignKey(VideoModel, on_delete=PROTECT, db_column='video_id')
    product_id = ForeignKey(ProductModel, on_delete=PROTECT, db_column='product_id')

    class Meta:
        """Класс мета с названием таблицы"""
        db_table = 'videos_products'
