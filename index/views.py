from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post

@login_required(login_url='login')
def index(request):

    posts = Post.objects.all()

    context = {
        "user": request.user,
        "posts": posts
    }

    return render(request, "index/index.html", context)
