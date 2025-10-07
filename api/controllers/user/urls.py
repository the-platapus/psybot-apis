from django.urls import path
from .views import register_user, login_user, update_profile, delete_profile

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('update/', update_profile, name='update_profile'),
    path('delete/', delete_profile, name='delete_profile'),
]