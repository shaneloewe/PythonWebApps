from requests import get
from django.core.management.base import BaseCommand
from hero.models import Superhero
from json import dump


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = [s for s in Superhero.objects.all().values()]
        path = "C:/Users/shane/OneDrive/Desktop/myData.json"
        print("Exporting data to "+path)
        # Write to JSON File
        with open(path, "w") as f:
            dump(data, f, indent=4)
