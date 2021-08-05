from rest_framework import serializers
from mainpage.models import PageSettings, Contacts, PageContent


class PageSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSettings
        exclude = ("modified_at", "addition_code", "insert_addition_code")
    user = serializers.StringRelatedField(read_only=True)
    additions = serializers.SerializerMethodField()
    flag = serializers.SerializerMethodField()

    def get_additions(self, instance):
        return instance.addition_code

    def get_flag(self, instance):
        return instance.insert_addition_code
