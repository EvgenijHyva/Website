from rest_framework import serializers
from users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password", "user_permissions", "groups", "age", "is_staff", "email", "is_superuser", "is_active")

    phone = serializers.SerializerMethodField()

    def get_phone(self, instance):
        phone = str(instance.phone)
        return phone[0:len(phone)-4] + 4 * "*" if len(phone)>4 else None
