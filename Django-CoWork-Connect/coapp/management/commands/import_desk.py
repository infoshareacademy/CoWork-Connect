from django.core.management.base import BaseCommand
import json
from pathlib import Path
from django.conf import settings
from coapp.models import Desk

class Command(BaseCommand):
    help = 'Imports desks from a JSON file into the database'

    def handle(self, *args, **options):
        # Użycie settings.BASE_DIR pozwala na odwołanie się do katalogu głównego projektu Django
        # Path() z pathlib pozwala na eleganckie i systemowo niezależne budowanie ścieżek
        json_file_path = Path(settings.BASE_DIR) / 'coapp' / 'management' / 'commands' / 'desks.json'

        with open(json_file_path, 'r') as file:
            desks = json.load(file)
            for desk_id, desk_info in desks.items():
                Desk.objects.create(
                    desk_type=desk_info["desk_type"],
                    monitor=desk_info["monitor"],
                    size=desk_info["rozmiar"],
                    price=desk_info["price"],
                    status=desk_info["status"],
                    name=desk_info["name"]
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported desks'))