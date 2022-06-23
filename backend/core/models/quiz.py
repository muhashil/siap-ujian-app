from typing import Optional, Iterable

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from backend.core.storage import get_file_storage_system
from backend.core.models.mixins import TimeStampedModel
from backend.core.models.enum import KategoriMateri, TipeMateri, AnswerCharacter, ImageSource


class Quiz(TimeStampedModel):
    type = models.CharField(max_length=25, choices=TipeMateri.choices)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return f"{self.get_type_display()} - {self.title}"

    def save(self, force_insert: bool = False, force_update: bool = False, using: Optional[str] = None, update_fields: Optional[Iterable[str]] = None) -> None:
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{self.pk}"
        return super().save(force_insert, force_update, using, update_fields)


    class Meta:
        db_table = 'quizes'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'


class Question(TimeStampedModel):
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE, null=True, blank=True)
    # number = models.IntegerField(default=1, 
    #                              validators=[MinValueValidator(limit_value=1), 
    #                                          MaxValueValidator(limit_value=1000)])
    category = models.CharField(max_length=25, choices=KategoriMateri.choices)
    question = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    sumber = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text='Question answer explanation.')

    def __str__(self) -> str:
        return self.question

    def save(self, force_insert: bool = False, force_update: bool = False, using: Optional[str] = None, update_fields: Optional[Iterable[str]] = None) -> None:
        if not self.slug:
            title_sliced = self.question[:50]
            self.slug = f"{slugify(title_sliced)}-{self.pk}"
        return super().save(force_insert, force_update, using, update_fields)


    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        # constraints = [
        #     models.UniqueConstraint(fields=['number', 'quiz'], name='quiz unique question number'),
        # ]


class QuestionImage(TimeStampedModel):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    source = models.CharField(max_length=25, choices=ImageSource.choices)
    image = models.ImageField(storage=get_file_storage_system)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'question_images'
        verbose_name = 'Question Image'
        verbose_name_plural = 'Question Images'



class Answer(TimeStampedModel):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=2, choices=AnswerCharacter.choices)
    answer = models.CharField(max_length=250)
    is_true = models.BooleanField(default=False, verbose_name='Is Correct?')

    def __str__(self) -> str:
        return f"{self.question.question} - {self.option}. {self.answer}"


    class Meta:
        db_table = 'answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
