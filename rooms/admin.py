from django.contrib import admin
from .models import Room, Amenity
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  list_display = ("name", "country", "city", "price", "address", "bathrooms", "bedrooms", "room_type", "description", "owner", "house"
                  ,"amenities_count", "total_amenities", "rating")
  list_filter = ("room_type", "house", "amenities")
  search_fields = ("name", "^price", "owner__username", "house__name", "country", "city", "address", "description") 
  actions = ["set_prices_to_zero"]
  
  def total_amenities(self, room):
    return room.amenities.count() + 2
    
  def set_prices_to_zero(self, request, queryset):
    updated_count = queryset.update(price=0)
    self.message_user(request, f"{updated_count}개의 방 가격이 0으로 설정되었습니다.")
  set_prices_to_zero.short_description = "선택한 방들의 가격을 0으로 설정"

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "created", "updated")
  search_fields = ("name", "description")
  readonly_fields = ("created", "updated")
  pass