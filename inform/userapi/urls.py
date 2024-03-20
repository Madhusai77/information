# urls.py

from django.urls import path
from .views import create_user, get_user, update_user

urlpatterns = [
    path('users/', create_user),
    path('users/<int:user_id>/', get_user),
    path('users/<int:user_id>/update/', update_user),
]
