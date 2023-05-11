from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from .decorators import already_logged_in



@already_logged_in
def register(request):

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_id = user.id
            user.save()
            auth.login(request, user)
            return redirect('profile', user_id=user_id)

    context = {
        "form": form
    }
    
    return render(request, 'accounts/register.html', context)


@already_logged_in
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


@login_required(login_url='login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("login")
    return HttpResponse("<h2>You are not logged in!!!</h2>")





        

