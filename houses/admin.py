from django.contrib import admin
from .models import House

@admin.register(House) #Registsers the House model with the admin site
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'year', 'area', 'bedrooms', 'bathrooms', 'floors', 'parking', 'garden', 'pool', 'image', 'pets_allowed')
    list_filter = ('price', 'year', 'area', 'bedrooms', 'bathrooms', 'floors', 'parking', 'garden', 'pool', 'pets_allowed')
    list_editable = ('price','pets_allowed')
    search_fields = (['address__startswith', 'name'])
    exclude = ('image',) #Excludes the image field from the form