from django.db import transaction
from database.models.user import User
from database.serializers.user_serializer import UserSerializer
from bson.objectid import ObjectId

# Services as functions

def create_user(data):
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    with transaction.atomic():
        user = serializer.save(action_type=1)  # created -> 1
    return UserSerializer(user).data


def login_user(email: str, password: str):
    """Login by verifying email and password. Assumes plaintext or pre-hashed comparison handled upstream."""
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValueError("Invalid email or password")
    if user.password != password:
        raise ValueError("Invalid email or password")
    return UserSerializer(user).data


def update_profile(user_id: str, update_data: dict):
    """Update allowed user fields by user_id (ObjectId)."""
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise ValueError("Invalid user_id format; must be a 24-char hex ObjectId")
    try:
        user = User.objects.get(pk=obj_id)
    except User.DoesNotExist:
        raise ValueError("User not found for provided user_id")

    allowed_fields = {"name", "email", "password", "dob"}
    sanitized = {k: v for k, v in update_data.items() if k in allowed_fields}
    if not sanitized:
        raise ValueError("No valid fields to update")

    for k, v in sanitized.items():
        setattr(user, k, v)
    with transaction.atomic():
        user.action_type = 2  # updated
        user.save(update_fields=list(sanitized.keys()) + ["action_type", "updated_at"])
    return UserSerializer(user).data


def delete_profile(user_id: str):
    """Delete a user by ObjectId. Related chatheads and messages will be deleted via cascade FKs."""
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise ValueError("Invalid user_id format; must be a 24-char hex ObjectId")
    try:
        user = User.objects.get(pk=obj_id)
    except User.DoesNotExist:
        raise ValueError("User not found for provided user_id")

    with transaction.atomic():
        # mark as deleted before actual deletion (chatheads and messages cascade)
        user.action_type = 3
        user.save(update_fields=["action_type", "updated_at"])
        user.delete()
    return {"deleted": True, "deleted_count": 1}