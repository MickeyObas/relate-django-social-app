from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def no_of_likes(self, obj):
        return LikePost.objects.filter(post=obj).count()

    def __str__(self):
        return f"Post by {self.owner}"
    
    
from like.models import LikePost