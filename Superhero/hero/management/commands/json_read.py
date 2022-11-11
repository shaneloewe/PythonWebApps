from requests import get
from django.core.management.base import BaseCommand
from hero.models import Superhero
from pathlib import Path
from json import loads


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = Path("C:/Users/shane/OneDrive/Desktop/myData.json")
        print("Importing data...")
        # Read from JSON File
        if path.exists():
            objects = loads(path.read_text())

        for o in objects:
            Superhero.objects.get_or_create(**o)
