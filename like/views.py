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
            post.no_of_likes -= 1
            post.save(update_fields=['no_of_likes'])

        else:
            LikePost.objects.create(post=post, user=user)
            post.no_of_likes += 1
            post.save(update_fields=['no_of_likes'])

        return redirect('index')
        

def like_comment(request, pk):
     
     comment = get_object_or_404(Comment, id=pk)
     user = request.user
     comment_liked = LikeComment.objects.filter(comment=comment, user=user)

     if comment_liked:
          comment_liked.delete()
          comment.no_of_likes -= 1
          comment.save(update_fields=['no_of_likes'])
     else:
          LikeComment.objects.create(comment=comment, user=user)
          comment.no_of_likes += 1
          comment.save(update_fields=['no_of_likes'])
        
     return redirect('index')
   

        

