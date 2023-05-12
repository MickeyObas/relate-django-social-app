from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser
from .models import Follow


@login_required(login_url='login')
def follow(request, u_pk):

    if request.method == 'POST':

        follower = get_object_or_404(CustomUser, id=request.user.id)
        user = get_object_or_404(CustomUser, id=u_pk)
        follow_object = Follow.objects.filter(follower=follower, user=user).first()

        if follow_object:
            follow_object.delete()
            return redirect('profile', user.id)

        Follow.objects.create(follower=follower, user=user)
        return redirect('profile', user_id=user.id)

    return HttpResponse("<h3>Wetin you dey do?</h3>")

