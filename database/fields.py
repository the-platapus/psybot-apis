from django.db import models
from bson.objectid import ObjectId


class DevObjectIdField(models.CharField):
    """
    A simple CharField that mimics a MongoDB ObjectId for local SQLite testing.
    It stores the ObjectId as a 24-character hex string and auto-generates a
    default value when none is provided.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 24)
        # Allow primary_key to be passed through
        default = kwargs.get('default', None)
        if default is None:
            kwargs['default'] = lambda: str(ObjectId())
        super().__init__(*args, **kwargs)
