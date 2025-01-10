from django.contrib import admin
from .models import Room, Message
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__",)
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message", "room", "user", "created", "updated")
    pass
