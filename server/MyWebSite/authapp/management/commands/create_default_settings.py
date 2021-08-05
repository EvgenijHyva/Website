from django.core.management import BaseCommand
from mainpage.models import PageSettings
from users.models import CustomUser


class Command(BaseCommand):
    help = "Create a default settings for a new user, if user settings doesnt created automatically "

    def handle(self, *args, **options):
        no_settings = CustomUser.objects.filter(user_settings__isnull=True)
        if no_settings:
            for user in CustomUser.objects.filter(user_settings__isnull=True):
                PageSettings.objects.create(user=user)
            print(f"{no_settings.count()} users without settings repaired")
        else:
            print("All users have a settings in db. Nothing to repair")
