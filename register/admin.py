from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # 追加したフィールドもadminで確認できるように
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image', 'likes',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('image', 'likes',)}),
    )


admin.site.register(User, CustomUserAdmin)
