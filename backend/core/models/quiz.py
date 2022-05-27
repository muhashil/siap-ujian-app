from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from backend.core.models.mixins import TimeStampedModel
from backend.core.models.enum import KategoriMateri, TipeMateri, AnswerCharacter


class Quiz(TimeStampedModel):
    type = models.CharField(max_length=25, choices=TipeMateri.choices)
    title = models.CharField(max_length=250)

    class Meta:
        db_table = 'quizes'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'


class Question(TimeStampedModel):
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    number = models.IntegerField(default=1, 
                                       validators=[MinValueValidator(limit_value=1), 
                                                   MaxValueValidator(limit_value=1000)])
    category = models.CharField(max_length=25, choices=KategoriMateri.choices)
    question = models.CharField(max_length=250)
    sumber = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, help_text='Question answer explanation.')

    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(TimeStampedModel):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=2, choices=AnswerCharacter.choices)
    answer = models.CharField(max_length=250)
    is_true = models.BooleanField(default=False)


    class Meta:
        db_table = 'answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
