from django.db import models
from common.models import CommomModel
from django.core.exceptions import ValidationError

class Review(CommomModel):
  '''review will be sent to rooms or experiences. only one of them will be used'''
  
  user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
  review = models.TextField()
  
  room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
  experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, related_name="experiences", null=True, blank=True)
  
  rating = models.PositiveIntegerField()
  
  def __str__(self):
     return f"{self.user} / {self.rating}"
  
  def clean(self):
      super().clean()
      if not (1 <= self.rating <= 5):
          raise ValidationError('Rating must be between 1 and 5.')
      if self.room and self.experience:
          raise ValidationError('Review can be associated with either a room or an experience, not both.')
      if not self.room and not self.experience:
          raise ValidationError('Review must be associated with either a room or an experience.')

  def save(self, *args, **kwargs):
      self.clean()  # Ensure custom validation is performed
      super().save(*args, **kwargs) 
      
      def formfield(self, **kwargs):
        return super().formfield(
            **{
                "min_value": 1,
                "max_value": 5,
                **kwargs,
            }
        )