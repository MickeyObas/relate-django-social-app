from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post
from like.models import LikePost, LikeComment

@login_required(login_url='login')
def index(request, **kwargs):
    
    posts_liked = []
    comments_liked = []

    posts = Post.objects.all()[:5]

    for post in posts:

        comments = post.comment_set.all()

        if LikePost.objects.filter(post=post, user=request.user).exists():
            posts_liked.append(post)
        for comment in comments:
            if LikeComment.objects.filter(comment=comment, user=request.user).exists():
                comments_liked.append(comment)

    context = {
        "user": request.user,
        "posts": posts,
        "posts_liked": posts_liked,
        "comments_liked": comments_liked
    }

    return render(request, "index/index.html", context)
