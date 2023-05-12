from django.shortcuts import redirect
from django.contrib import messages



def already_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, message="You are already logged in!")
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

