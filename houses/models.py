from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import User

# Create your models here.
class House(models.Model): #TODO: Fieldset 추가하기
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year = models.PositiveBigIntegerField()
    area = models.PositiveIntegerField(help_text='m²')
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.FloatField()
    floors = models.PositiveIntegerField()
    parking = models.BooleanField()
    garden = models.BooleanField()
    pool = models.BooleanField()
    image = models.ImageField(upload_to='houses/images', blank=True, null=True)
    pets_allowed = models.BooleanField(default=False, verbose_name='Pets allowed?')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.name