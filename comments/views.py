from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from .models import Comment
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

def comment_delete(request, pk):

    comment = get_object_or_404(Comment, id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    
    return render (request, "comments/comment_delete.html")


        
