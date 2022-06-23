from typing import Dict, Sequence, Optional

from django.contrib import admin

from backend.core.models.user import User
from backend.core.models.banner import Banner
from backend.core.models.materi import Materi
from backend.core.models.quiz import QuestionImage, Quiz, Question, Answer


class UserAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


class MateriAdmin(admin.ModelAdmin):
    prepopulated_fields: Dict[str, Sequence[str]] = {"slug": ("title",)}


class QuizAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['option', 'answer', 'is_true']
    extra: int = 4
    max_num: Optional[int] = 4

class QuestionImageInline(admin.TabularInline):
    model = QuestionImage
    fields = ['title', 'image', 'source']
    extra: int = 1


class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields: Sequence[str] = ['quiz']
    inlines = [
        AnswerInline,
        QuestionImageInline
    ]

class AnswerAdmin(admin.ModelAdmin):
    raw_id_fields: Sequence[str] = ['question']


class QuestionImageAdmin(admin.ModelAdmin):
    raw_id_fields: Sequence[str] = ['question']


admin.site.register(User, UserAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Materi, MateriAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionImage, QuestionImageAdmin)
