from allauth.account.adapter import get_adapter
from rest_framework import serializers

from users.models import GENDER_CHOICES
from users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password", "user_permissions", "groups", "is_staff", "is_superuser", "is_active",)
        read_only_fields = ("last_login", "date_joined", "city")

    phone = serializers.IntegerField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data
