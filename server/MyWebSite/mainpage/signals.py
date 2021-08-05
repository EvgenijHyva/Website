from django.db.models.signals import post_save
from django.dispatch import receiver

from mainpage.models import PageSettings
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_user_settings(sender, instance, created, **kwargs):
    """Signals post create settings after creating new user.
    Completing the registration of signal in mainpage.apps and __init__.py"""
    if created:
        PageSettings.objects.create(user=instance)
        print(f"user {instance}'s settings created by mainpage.signal.py")
    else:
        instance.user_settings.save()
