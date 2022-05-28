from django.db import models

from backend.core.models.mixins import TimeStampedModel


class Banner(TimeStampedModel):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/banner/')
    url = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

