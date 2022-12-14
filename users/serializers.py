from rest_framework import serializers
from users.models import User

class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'id', 'first_name', 'last_name']