from django.urls import path, include
from . import views

urlpatterns = [
    path("create-post", views.post_create, name="create-post"),
    path("<str:pk>/update-post", views.post_update, name="update-post"),
    path("<str:pk>/delete-post", views.post_delete, name="delete-post"),

    path('<str:pk>/like-post/', include('like.urls')),
    path('<str:pk>/comment/', include('comments.urls')),
]