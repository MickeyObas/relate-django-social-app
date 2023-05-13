from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.comment_post,  name='comment-post'),
    path('delete', views.comment_delete,  name='comment-delete')
]