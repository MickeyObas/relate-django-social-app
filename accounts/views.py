from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth, messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>You are in!!!</h1>")
        
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

    context = {
        "user": request.user
    }

    return render(request, "accounts/index.html", context)