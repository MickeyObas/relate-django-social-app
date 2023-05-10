from django.urls import path
from . import views


urlpatterns = [
    path('', views.comment_post,  name='comment-post')
]