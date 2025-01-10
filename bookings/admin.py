from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'kind',
    'user',
    'room',
    'experience',
    'check_in',
    'check_out',
    'experience_time',
    'guests',
  )
  list_filter = (
    'kind',
    'check_in',
    'check_out',
    'experience_time',
  )
  search_fields = (
    'user__username',
    'room__name',
    'experience__name',
  )
  raw_id_fields = (
    'user',
    'room',
    'experience',
  )
  date_hierarchy = 'check_in'
  ordering = (
    'check_in',
    'check_out',
  )
  readonly_fields = (
    'created',
    'updated',
  )
  fieldsets = (
    (
      None,
      {
        'fields': (
          'kind',
          'user',
          'room',
          'experience',
          'check_in',
          'check_out',
          'experience_time',
          'guests',
        ),
      },
    ),
    (
      'History',
      {
        'fields': (
          'created',
          'updated',
        ),
      },
    ),
  )
  # def get_readonly_fields(self, request, obj=None):
  #   if obj:
  #     return self.readonly_fields + ('user', 'room', 'experience',)
  #   return self.readonly_fields
  # def has_add_permission(self, request):
  #   return False
  # def has_delete_permission(self, request, obj=None):
  #   return False
  # def has_change_permission(self, request, obj=None):
  #   return False
  # def has_view_permission(self, request, obj=None):
  #   return True
