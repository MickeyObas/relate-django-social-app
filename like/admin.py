from django.contrib import admin

from .models import LikeComment, LikePost

admin.site.register(LikePost)
admin.site.register(LikeComment)
