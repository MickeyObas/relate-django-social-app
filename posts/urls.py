from django.urls import path
from . import views

urlpatterns = [
    path("create-post", views.post_create, name="create-post"),
    path("<int:pk>/update-post", views.post_update, name="update-post"),
    path("<int:pk>/delete-post", views.post_delete, name="delete-post")
]