from rest_framework import serializers
from users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password", "user_permissions", "groups", "age", "is_staff", "email", "is_superuser"]
