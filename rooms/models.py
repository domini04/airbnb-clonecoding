from django.db import models
from common.models import CommomModel
from django.forms import ValidationError

# Create your models here.
class Room(CommomModel):
  class RoomTypeChoices(models.TextChoices):
    ENTIRE = ("Entire", "건물 전체")
    PRIVATE = ("Private", "개인실")
    SHARED = ("Shared", "다인실")
    HOTEL = "Hotel"
  
  def clean(self):
      if self.bathrooms % 0.5 != 0:
          raise ValidationError('Bathrooms must be in increments of 0.5')

  def save(self, *args, **kwargs):
      self.clean()
      super().save(*args, **kwargs)
      
  def __str__(self):
      return self.name + " - " + self.house.name
    
  def rating(self):
      reviews = self.reviews.all()
      if not reviews:
          return "n/a"
      avg = 0
      for review in reviews.values("rating"):
          avg += review["rating"]
      return round(avg / len(reviews), 2)
    
  name = models.CharField(max_length=100, default="")  
  country = models.CharField(max_length=50, default="대한민국")
  city = models.CharField(max_length=50, default="서울") 
  price = models.PositiveIntegerField()
  address = models.CharField(max_length=140)
  bathrooms = models.FloatField()
  bedrooms = models.PositiveIntegerField()
  room_type = models.CharField(max_length=10, choices=RoomTypeChoices.choices)  
  description = models.TextField()
  
  owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")
  house = models.ForeignKey("houses.House", on_delete=models.CASCADE, related_name="rooms")
  amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms", blank=True)
  category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="rooms")
  
  def amenities_count(self):
      return self.amenities.count()

class Amenity(CommomModel):
  name = models.CharField(max_length=80)
  description = models.TextField(blank=True)
    
  def __str__(self) -> str:
      return self.name
    
  class Meta:
    verbose_name_plural = "Amenities"