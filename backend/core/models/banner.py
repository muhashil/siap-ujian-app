from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from backend.core.models.mixins import TimeStampedModel
from backend.core.storage import get_file_storage_system



class Banner(TimeStampedModel):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(storage=get_file_storage_system)
    url = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

