from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
    )
    filter_horizontal = ("rooms", "experiences")
    search_fields = ("name",)
    list_filter = ("user",)
    raw_id_fields = ("user",)
    readonly_fields = ("created", "updated")