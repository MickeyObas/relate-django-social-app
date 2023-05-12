from django.urls import path
from . import views


urlpatterns = [
    path('<int:u_pk>', views.follow, name='follow')
]