from django.urls import path

from . import views

urlpatterns = [
    path('', views.like_post, name='like-post')
]