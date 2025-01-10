from django.contrib import admin
from .forms import ExperienceForm
from .models import Experience, Perk
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
  """Experience Admin Definition"""
  form = ExperienceForm
  
  def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    form.base_fields['duration'].label = 'Duration (hrs)'
    form.base_fields['price'].label = 'Price ($)'
    return form

  def price_with_currency(self, obj):
    return f'{obj.price}'
  price_with_currency.short_description = 'Price ($)'


  list_display = (
    'name',
    'host',
    'country',
    'city',
    'price_with_currency',
    'duration',
    'starts_at',
    'ends_at',
  )

  list_filter = ("category",)
  
@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
  """Perk Admin Definition"""
  pass