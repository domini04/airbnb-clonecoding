from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # fields = ("email", "password", "name", "is_host", "is_active", "is_staff", "is_superuser")
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "email", "is_host", "profile_image", "gender", "language", "currency"),  
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
                "classes": ("collapse",),
                },
        ),
        (
          "Important dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            }  
        )
    )
    list_display = ("username", "email", "is_host")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )