from django.db import models
from Users.models import User_Profile

class Tracking(models.Model):
    users = models.ForeignKey(User_Profile , on_delete=models.CASCADE)
    current_position_details = models.TextField()
    current_position_latitude = models.TextField()
    current_position_longitude = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.users.user)
    

# Create your models here.
