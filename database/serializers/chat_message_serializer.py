from rest_framework import serializers
from database.models.chat_message import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['_id', 'chat_head', 'user_message', 'agent_reply', 'action_type', 'created_at', 'updated_at']
        extra_kwargs = {
            'chat_head': {'read_only': True}
        }