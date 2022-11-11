from requests import get
from django.core.management.base import BaseCommand
from hero.models import Superhero
from csv import writer


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = "C:/Users/shane/OneDrive/Desktop/myData.json"
        [[s.name, s.author, s.path] for s in Superhero.objects.all()]
        print("Exporting data to "+path)
        # Write to JSON File
        with open(path, "w", newline='') as f:
            writer(f).writerows(table)
