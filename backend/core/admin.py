from backend.core.models.user import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)