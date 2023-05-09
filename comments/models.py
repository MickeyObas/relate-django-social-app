from django.db import models

from accounts.models import CustomUser 

class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    picture = models.FileField(upload_to='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.body[:20], self.owner.email)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'