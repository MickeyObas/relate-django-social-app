from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostCreateForm


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

def post_update(request):
    pass

def post_delete(request):
    pass