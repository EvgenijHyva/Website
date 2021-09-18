from users.CustomException import CustomException
from users.models import GENDER_CHOICES
from django.db import transaction
from rest_framework import serializers, status
from dj_rest_auth.registration.serializers import RegisterSerializer


class AppRegisterSerializer(RegisterSerializer):
    gender = serializers.ChoiceField(GENDER_CHOICES)
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=30, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=150, allow_null=True, allow_blank=True)
    tos = serializers.BooleanField(default=False)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.user_name = self.data.get('name')
        user.email = self.data.get('email')
        user.phone = self.data.get("phone")
        user.first_name = self.data.get("first_name")
        user.last_name = self.data.get("last_name")
        if self.data.get("tos"):
            user.save()
            return user
        else:
            raise CustomException(detail={
                "required": "You have to accept TOS for account registration"
            }, status_code=status.HTTP_400_BAD_REQUEST)