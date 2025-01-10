from django.db import models
from common.models import CommomModel

class Category(CommomModel):
    class CategoryKindChoices(models.TextChoices):
      Rooms = "rooms", "Rooms"
      Experiences = "experiences", "Experiences"
  
    name = models.CharField(max_length=55)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices)
    
    class Meta:
      verbose_name_plural = "Categories"
    
    def __str__(self) -> str:
      return self.name
    