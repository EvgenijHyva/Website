import os
import json
from django.conf import settings
from django.core.management import BaseCommand

from users.models import CustomUser

FILE_PATH = os.path.join(settings.BASE_DIR, r"authapp/fixtures/")

def load_from_json(file_name):
    with open(FILE_PATH + file_name + ".json", "r", encoding="utf-8") as json_file:
        return json.load(json_file)

class Command(BaseCommand):

    help = "Fill users from database_backup and create a default superuser"

    def handle(self, *args, **options):
        users = load_from_json("users")
        CustomUser.objects.all().delete()
        [CustomUser.objects.create(**user) for user in users]

        def create_superusers():
            CustomUser.objects.create_superuser(username="Evgeny", password="Djangotest", email="evgeny.hyvarinen@gmail.com",
                                          age=29, city="Helsinki", last_name="Hyvärinen", first_name="Evgeny")

        create_superusers() if all(map(lambda x: x.username != "Evgeny", CustomUser.objects.all())) else None


