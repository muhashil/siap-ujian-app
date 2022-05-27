from django.db import models

class TipeMateri(models.TextChoices):
    SBMPTN = 'SBMPTN', 'Seleksi Bersama Masuk Perguruan Tinggi Negeri'
    CPNS = 'CPNS', 'Calon Pegawai Negeri Sipil'


class KategoriMateri(models.TextChoices):
    TIU = 'TIU', 'Tes Intelegensi Umum'
    TWK = 'TWK', 'Tes Wawasan Kebangsaan'
    TKP = 'TKP', 'Tes Karakteristik Pribadi'

class AnswerCharacter(models.TextChoices):
    A = 'A', 'Option A'
    B = 'B', 'Option B'
    C = 'C', 'Option C'
    D = 'D', 'Option D'

