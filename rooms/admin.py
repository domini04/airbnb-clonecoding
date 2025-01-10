from django.contrib import admin
from .models import Room, Amenity
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  list_display = ("name", "country", "city", "price", "address", "bathrooms", "bedrooms", "room_type", "description", "owner", "house"
                  ,"amenities_count", "total_amenities", "rating")
  list_filter = ("room_type", "house", "amenities")
  search_fields = ("name", "^price","owner__username", "house__name") 
  
  def total_amenities(self, room):
    return room.amenities.count() + 2
  pass

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "created", "updated")
  
  readonly_fields = ("created", "updated")
  pass