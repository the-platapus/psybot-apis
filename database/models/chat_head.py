from djongo import models


class ChatHead(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey('database.User', on_delete=models.CASCADE, related_name="chat_heads")
    user_message = models.TextField()
    agent_reply = models.TextField()
    action_type = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat_head'