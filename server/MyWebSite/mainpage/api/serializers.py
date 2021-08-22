from django.shortcuts import get_object_or_404
from rest_framework import serializers
from mainpage.models import PageSettings, Contacts, PageContent


class PageSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSettings
        exclude = ("modified_at", "addition_code", "insert_addition_code")
    user = serializers.StringRelatedField(read_only=True)
    additions = serializers.SerializerMethodField(read_only=True)
    flag = serializers.SerializerMethodField(read_only=True)

    def get_additions(self, instance):
        if instance.insert_addition_code:
            return instance.addition_code
        else:
            return None

    def get_flag(self, instance):
        return instance.insert_addition_code


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        exclude = ("updated_at","id", "created_at")

    telegram_username = serializers.SerializerMethodField()
    whatsapp = serializers.SerializerMethodField()

    # https://www.kobzarev.com/programming/links-to-whatsapp-and-telegram/ direct link

    user_is_authorized = serializers.SerializerMethodField(read_only=True)

    def get_user_is_authorized(self, instance):
        request = self.context.get("request")
        return str(request.user) != "AnonymousUser"

    def get_telegram_username(self, instance):
        return f"https://t.me/{instance.telegram_username}"

    def get_whatsapp(self, instance):
        return f"https://wa.me/{instance.whatsapp}"

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        exclude = ("created_at", "updated_at", "show_image", "id", )
    post_number = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        if instance.show_image:
            return instance.image if instance.image else None
        else:
            return None

    def get_post_number(self, instance):
        return instance.id
