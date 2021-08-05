import json
from authapp.management.commands.db_fill import FILE_PATH
from django.core.management import BaseCommand
from django.core import serializers

from users.models import CustomUser


class Command(BaseCommand):

    help = "Copy database to json file"

    def handle(self, *args, **options):
        files_db = {
            "users": CustomUser.objects.all(),

        }
        [self.dump_json(i, k) for i, k in files_db.items()]

    def dump_json(self, new_file_name, content):
        content_serial = serializers.serialize("json", content)
        with open(FILE_PATH + new_file_name + ".json", "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(json.loads(content_serial), indent=4, ensure_ascii=False))
