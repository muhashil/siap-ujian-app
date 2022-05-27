from django.db import models
from backend.core.models.mixins import TimeStampedModel
from backend.core.models.enum import KategoriMateri, TipeMateri

class Materi(TimeStampedModel):
    type = models.CharField(max_length=25, choices=TipeMateri.choices)
    category = models.CharField(max_length=25, choices=KategoriMateri.choices)
    title = models.CharField(max_length=250)
    content = models.TextField()
    file = models.FileField(upload_to='uploads/materi/', null=True)

    class Meta:
        db_table = 'materi'
        verbose_name = 'Materi'
        verbose_name_plural = 'Materi'
