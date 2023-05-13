from django.db import models
from accounts.models import CustomUser

import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    no_of_likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.owner}"
    
    class Meta:
        ordering = ['-created']
    
