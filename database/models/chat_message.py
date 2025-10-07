from djongo import models
from .chat_head import ChatHead

class ChatMessage(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    chat_head = models.ForeignKey(ChatHead, on_delete=models.CASCADE, related_name="messages")
    user_message = models.TextField()
    agent_reply = models.TextField()
    action_type = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat_message'