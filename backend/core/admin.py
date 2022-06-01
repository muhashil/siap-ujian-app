from typing import Dict, Sequence

from django.contrib import admin

from backend.core.models.user import User
from backend.core.models.banner import Banner
from backend.core.models.materi import Materi
from backend.core.models.quiz import Quiz, Question, Answer


class UserAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


class MateriAdmin(admin.ModelAdmin):
    prepopulated_fields: Dict[str, Sequence[str]] = {"slug": ("title",)}


class QuizAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Materi, MateriAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
