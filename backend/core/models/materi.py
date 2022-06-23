from typing import Optional, Iterable

from django.db import models
from django.utils.text import slugify

from backend.core.models.mixins import TimeStampedModel
from backend.core.models.enum import KategoriMateri, TipeMateri

from backend.core.storage import get_file_storage_system

class Materi(TimeStampedModel):
    type = models.CharField(max_length=25, choices=TipeMateri.choices)
    category = models.CharField(max_length=25, choices=KategoriMateri.choices)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    file = models.FileField(storage=get_file_storage_system, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.get_category_display()} - {self.title}"

    def save(self, force_insert: bool = False, force_update: bool = False, using: Optional[str] = None, update_fields: Optional[Iterable[str]] = None) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)


    class Meta:
        db_table = 'materi'
        verbose_name = 'Materi'
        verbose_name_plural = 'Materi'
