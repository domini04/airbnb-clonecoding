from django.db import models
from common.models import CommomModel

class Booking(CommomModel):
  
  class BookingKindChoices(models.TextChoices):
    ROOM = 'ROOM', 'Room'
    EXPERIENCE = 'EXPERIENCE', 'Experience'
    
  kind = models.CharField(
    max_length=10,
    choices=BookingKindChoices.choices,
  )
  
  user = models.ForeignKey(
    'users.User',
    on_delete=models.CASCADE,
  )
  
  room = models.ForeignKey(
    'rooms.Room',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
  )
  
  experience = models.ForeignKey(
    'experiences.Experience',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
  )
  
  check_in = models.DateField(
    null=True,
    blank=True,
  )
  check_out = models.DateField(
    null=True,
    blank=True,
  )
  experience_time = models.DateTimeField(
    null=True,
    blank=True,
  )
  guests = models.PositiveIntegerField()
  
  def __str__(self):
    return f"{self.kind} - {self.room or self.experience}"