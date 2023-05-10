from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import CustomUserCreationForm, ProfileCreationForm
from posts.models import Post
from .models import Profile, CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_id = user.id
            user.save()
            return redirect('profile', user_id=user_id)
        
    form = CustomUserCreationForm()

    context = {
        "form": form
    }
    
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            print("Logged in!")
            auth.login(request, user)
            return redirect("index") # Index View not built out yet...
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("login")
        
    return render(request, "accounts/login.html")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("login")
    return HttpResponse("<h2>You are not logged in!!!</h2>")


def index(request):

    posts = Post.objects.all()

    context = {
        "user": request.user,
        "posts": posts
    }

    return render(request, "accounts/index.html", context)


def profile(request, user_id):

    user_object = get_object_or_404(CustomUser, id=user_id)
    profile_object = get_object_or_404(Profile, user=user_object)
    form = ProfileCreationForm(instance=profile_object)

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES, instance=profile_object)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)
        
    context = {
        "form": form,
        "user_object": user_object,
        "profile_object": profile_object
    }
        
    return render(request, "accounts/profile.html", context)
        

