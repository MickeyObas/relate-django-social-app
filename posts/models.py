from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/post_images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.owner}"
    
    
