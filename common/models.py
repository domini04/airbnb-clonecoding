from django.db import models

class CommomModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    
    class Meta: # Model이 abstract이므로 DB에 저장되지 않음
        abstract = True