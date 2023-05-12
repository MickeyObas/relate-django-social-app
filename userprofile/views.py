from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import CustomUser, Profile
from accounts.forms import ProfileCreationForm
from follow.models import Follow

@login_required(login_url='login')
def profile(request, user_id):

    user_object = get_object_or_404(CustomUser, id=user_id)
    profile_object = get_object_or_404(Profile, user=user_object)
    form = ProfileCreationForm(instance=profile_object)

    if request.method == 'POST':
        if request.POST.get('profile_save'):
            form = ProfileCreationForm(request.POST, request.FILES, instance=profile_object)
            if form.is_valid():
                form.save()
                return redirect('profile', user_id=user_id)
            else:
                messages.error(request, "Invalid data!")

    if Follow.objects.filter(user=user_object, follower=request.user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
        
    context = {
        "form": form,
        "user_object": user_object,
        "profile_object": profile_object,
        "button_text": button_text,
        "followers": user_object.followed_by.all().count()
    }
        
    return render(request, "accounts/profile.html", context)