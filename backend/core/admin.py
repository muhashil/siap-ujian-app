from backend.core.models.user import User
from backend.core.models.banner import Banner
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Banner, BannerAdmin)