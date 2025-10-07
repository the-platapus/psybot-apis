from django.urls import path
from .views import create_chat_head, list_chat_heads, get_chat_head, delete_chat_head

urlpatterns = [
    path('create/', create_chat_head, name='create_chat_head'),
    path('list/', list_chat_heads, name='list_chat_heads'),
    path('get/', get_chat_head, name='get_chat_head'),
    path('delete/', delete_chat_head, name='delete_chat_head'),
]