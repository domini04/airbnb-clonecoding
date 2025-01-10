from django.db import models
from common.models import CommomModel
# Create your models here.

class Experience(CommomModel):
  """Experience & Trips"""
  
  name = models.CharField(max_length=100, default="")
  host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="experiences")
  country = models.CharField(max_length=50, default="대한민국")
  city = models.CharField(max_length=50, default="서울") 
  price = models.PositiveIntegerField()
  duration = models.PositiveIntegerField()
  address = models.CharField(max_length=200)
  starts_at = models.DateTimeField()
  ends_at = models.DateTimeField()
  description = models.TextField()
  perks = models.ManyToManyField("Perk", related_name="experiences", blank=True)
  category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return self.name



class Perk(CommomModel):
  """Perk Model Definition"""
  
  name = models.CharField(max_length=80)
  details = models.TextField(blank=True)
  

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name_plural = "Perks"