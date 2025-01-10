from django.db import models
from common.models import CommomModel

class Photo(CommomModel):
  
  file = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
  description = models.TextField(blank=True)
  room = models.ForeignKey('rooms.Room', related_name='photos', on_delete=models.CASCADE)
  experience = models.ForeignKey('experiences.Experience', related_name='photos', on_delete=models.CASCADE)
  
  
class Video(CommomModel):
  
  file = models.FileField(upload_to='videos/%Y/%m/%d', blank=True)
  experience = models.OneToOneField('experiences.Experience', related_name='video', on_delete=models.CASCADE)