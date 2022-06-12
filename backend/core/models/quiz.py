from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from backend.core.models.mixins import TimeStampedModel
from backend.core.models.enum import KategoriMateri, TipeMateri, AnswerCharacter


class Quiz(TimeStampedModel):
    type = models.CharField(max_length=25, choices=TipeMateri.choices)
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.get_type_display()} - {self.title}"

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
    question = models.CharField(max_length=250)
    sumber = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text='Question answer explanation.')

    def __str__(self) -> str:
        return self.question

    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        # constraints = [
        #     models.UniqueConstraint(fields=['number', 'quiz'], name='quiz unique question number'),
        # ]


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
