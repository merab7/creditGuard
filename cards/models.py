from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    censored_number = models.CharField(max_length=16)
    is_valid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    


    def __str__(self) -> str:
        return f"{self.user.username}-{self.title}"
    
 

