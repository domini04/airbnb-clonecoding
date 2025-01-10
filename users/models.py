from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

class User(AbstractUser): #TODO: Fieldset 추가하기
    first_name = models.CharField(max_length=30, editable=False, help_text='First name')
    last_name = models.CharField(max_length=100, editable=False, help_text='Last name')
    email = models.EmailField(unique=True, blank=True, null=True,)
    name = models.CharField(max_length=100, help_text='Name of the property', default="")
    is_host = models.BooleanField(default=False, help_text='Check if the user is a host') #house모델에 owner로 등록되면 True로 변경되어야 함
    
    profile_image = models.ImageField(upload_to='users/images', blank=True, null=True)
    
    class GenderChoices(models.TextChoices):
        MALE = ("M", "Male")
        FEMALE = ("F", "Female")
        
    gender = models.CharField(max_length= 10, choices=GenderChoices.choices, blank=True,)
    
    class LanguageChoices(models.TextChoices):
        KOREAN = ("KR", "Korean")
        ENGLISH = ("EN", "English")
    
    language = models.CharField(max_length= 10, choices=LanguageChoices.choices, blank=True,)
    
    class CurrencyChoices(models.TextChoices):
        KRW = ("KRW", "Korean Won")
        USD = ("USD", "US Dollar")
    
    currency = models.CharField(max_length= 10, choices=CurrencyChoices.choices, blank=True,)

    def clean(self):
        super().clean()
        if self.email:
            if User.objects.exclude(pk=self.pk).filter(email=self.email).exists():
                raise ValidationError('User with this Email already exists.')

    def save(self, *args, **kwargs):
        if self.email =="":
            self.email = None
        self.clean()
        super().save(*args, **kwargs)