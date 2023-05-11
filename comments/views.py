from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Comment
from .forms import CommentForm
from posts.models import Post


@login_required(login_url='login')
def comment_post(request, *args, **kwargs):
    
    form = CommentForm()
    post_id = kwargs.get('pk')
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


@login_required(login_url='login')
def comment_delete(request, pk):

    comment = get_object_or_404(Comment, id=pk)

    if comment.owner != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    
    return render (request, "comments/comment_delete.html")


        
