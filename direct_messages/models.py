from django.db import models
from common.models import CommomModel

class Room(CommomModel):
    """room model"""
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField("users.User")
    
    def __str__(self):
        return f"Chat Room : {self.id}"
    
class Message(CommomModel):
    """message model"""
    
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} says: {self.message}"