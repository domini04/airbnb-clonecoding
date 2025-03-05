from django.contrib import admin
from .models import Room, Amenity
# Register your models here.

@admin.action(description="Reset prices to 0")
def reset_prices(modeladmin, request, rooms):
  print(request.user)
  updated_count = rooms.update(price=0)
  # Optionally add a message to show how many rooms were updated
  modeladmin.message_user(request, f"Reset prices for {updated_count} rooms")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  
  actions = [reset_prices]
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