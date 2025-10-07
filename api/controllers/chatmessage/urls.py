from django.urls import path
from .views import create_message, list_chat_messages, delete_chat_message, update_chat_message

urlpatterns = [
    path('create/', create_message, name='create_message'),
    path('list/', list_chat_messages, name='list_chat_messages'),
    path('delete/', delete_chat_message, name='delete_chat_message'),
    path('update/', update_chat_message, name='update_chat_message'),
]