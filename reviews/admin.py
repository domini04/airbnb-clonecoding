from django.contrib import admin
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "rating", "get_experience_name")
    list_filter = ("rating",)
    search_fields = ("user__username",)

    def get_experience_name(self, obj):
        return obj.experience.name if obj.experience else None
    get_experience_name.short_description = 'Experience'