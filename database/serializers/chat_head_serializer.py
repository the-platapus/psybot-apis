from rest_framework import serializers
from database.models.chat_head import ChatHead

class ChatHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHead
        fields = ['_id', 'user', 'user_message', 'agent_reply', 'action_type', 'created_at', 'updated_at']
        extra_kwargs = {
            'user': {'read_only': True}
        }