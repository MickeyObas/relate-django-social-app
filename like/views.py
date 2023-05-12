from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import BadRequest

from .models import LikePost, LikeComment
from posts.models import Post
from comments.models import Comment

def like_post(request, pk):
        
        post = get_object_or_404(Post, id=pk)
        user = request.user
        post_liked = LikePost.objects.filter(post=post, user=user)

        if post_liked:
            post_liked.delete()

        else:
            LikePost.objects.create(post=post, user=user)

        return redirect('index')
        
   

        

