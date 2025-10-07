from rest_framework import serializers
from database.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'password', 'dob', 'created_at', 'updated_at', 'action_type']