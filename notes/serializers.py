from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = Note
        fields = ['id','users', 'title', 'content', 'pin', 'date_created']