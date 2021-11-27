from rest_framework import serializers
from mainpage.models import PageSettings, Contacts, PageContent
from users.models import GENDER_CHOICES


class PageSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSettings
        exclude = ("modified_at", "addition_code", "insert_addition_code")
    user = serializers.SerializerMethodField(read_only=True)
    additions = serializers.SerializerMethodField(read_only=True)
    flag = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    def get_is_admin(self, instance):
        return instance.user.is_staff

    def get_user(self, instance):
        return instance.user.username

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
        return f"https://telegram.im/{instance.telegram_username}"

    def get_whatsapp(self, instance):
        return f"https://wa.me/{instance.whatsapp}"

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        exclude = ("created_at", "updated_at", "show_image", "id", )

    meta_choices = serializers.SerializerMethodField(read_only=True)
    post_number = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_meta_choices(self, instance):
        return {gender[1]: gender[0] for gender in GENDER_CHOICES}

    def get_image(self, instance):
        if instance.show_image and hasattr(instance.image, "url"):
            request = self.context.get("request")
            return request.build_absolute_uri(instance.image.url) if instance.image else None
        else:
            return None

    def get_post_number(self, instance):
        return instance.id
