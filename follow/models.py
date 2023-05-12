from django.db import models
from accounts.models import CustomUser

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followed_by')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} followed {self.user}"
