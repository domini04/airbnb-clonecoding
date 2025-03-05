from django.contrib import admin
from . import models

class WordFilter(admin.SimpleListFilter):
    title = "Search by word"
    parameter_name = "review"
    
    def lookups(self, request, model_admin):
        return [("good", "Good"), ("great", "Great"), ("awesome", "Awesome")]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(review__icontains=self.value())
        return queryset

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "rating", "get_experience_name")
    list_filter = ("rating","user__is_host", "room__category", WordFilter)
    search_fields = ("user__username",)

    def get_experience_name(self, obj):
        return obj.experience.name if obj.experience else None
    get_experience_name.short_description = 'Experience'