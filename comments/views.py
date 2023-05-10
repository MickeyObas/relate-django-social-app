from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from .forms import CommentForm

def comment_post(request, *args, **kwargs):
    
    post_id = kwargs.get('pk')
    form = CommentForm()
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.post = post
            comment.save()
            return redirect('index')

    context = {
        "form": form
    }

    return render(request, "comments/comment.html", context)

        
