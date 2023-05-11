from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostCreateForm, PostUpdateForm
from .models import Post


@login_required(login_url='login')
def post_create(request):

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("index")

    form = PostCreateForm()
    

    context = {
        "form": form
    }

    return render(request, "posts/create.html", context)


@login_required(login_url='login')
def post_update(request, pk):

    post = get_object_or_404(Post, id=pk)
    form = PostUpdateForm(instance=post)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            print(f"Post: Owner-{post.owner}, Content-{post.body}")
            post.save()
            return redirect('index')
        
    context = {
        "form": form
    }

    return render(request, "posts/update.html", context)


@login_required(login_url='login')
def post_delete(request, pk):
    
    post = get_object_or_404(Post, id=pk)
    print(post.id)

    context = {
        "post": post
    }

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Your Post has been deleted.")
        return redirect('index')
    
    return render(request, "posts/delete.html", context)